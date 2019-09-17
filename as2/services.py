import os
import email.utils
import shutil
import time
import requests

from django.utils.translation import ugettext as _
from django.dispatch import receiver
from django.db.models.signals import post_save

from as2 import models
from as2 import as2lib
from as2 import as2utils
from as2 import pyas2init

from as2.models import Routes, MessageReceived


class RouteFiles():
    def __init__(self):
        pass

    """
     Sends an AS2 encrypted message to a Configured Partner
    """

    @staticmethod
    def send(data):

        # get the incoming data
        organization = data["sender"];
        partner = data["receiver"];
        payload = data["file"];


        try:
            # Get the Orginzation, this is the Source of the message
            org = models.Organization.objects.get(name=organization)
        except models.Organization.DoesNotExist:
            raise Exception(_(u'Organization "%s" does not exist' % organization))
        try:
            # Get the Partner, this is the destination of the message
            partner = models.Partner.objects.get(name=partner)
        except models.Partner.DoesNotExist:
            raise Exception(_(u'Partner "%s" does not exist' % partner))

        # Check if payload (file on the system to be sent to a partner) exists and we have the right permissions
        if not os.path.isfile(payload):
            raise Exception(_(u'Payload at location "%s" does not exist' % payload))
        # The file will be deleted after it is sent, so make sure it can be.
        if not os.access(payload, os.W_OK):
            raise Exception('Insufficient file permission for payload %s' % payload)

        # Copy the file to the store
        output_dir = as2utils.join(pyas2init.gsettings['payload_send_store'], time.strftime('%Y%m%d'))
        # Check the dir
        as2utils.dirshouldbethere(output_dir)
        outfile = as2utils.join(output_dir, os.path.basename(payload))
        # Copy the payload to the out file
        shutil.copy2(payload, outfile)

        # Delete original payload file if option is set
        os.remove(payload)

        # Create the payload and message objects
        payload = models.Payload.objects.create(name=os.path.basename(payload),
                                                file=outfile,
                                                content_type=partner.content_type)

        # Create the message and add the payload to the message
        message = models.Message.objects.create(message_id=email.utils.make_msgid().strip('<>'),
                                                partner=partner,
                                                organization=org,
                                                direction='OUT',
                                                status='IP',
                                                payload=payload)

        # Build and send the AS2 message
        try:
            payload = as2lib.build_message(message)
            as2lib.send_message(message, payload)
        except Exception, e:
            pyas2init.logger.error(_(u'Failed to send message, error:\n%(txt)s') % {'txt': as2utils.txtexc()})
            message.status = 'E'
            models.Log.objects.create(message=message, status='E', text=_(u'Failed to send message, error is %s' % e))
            message.save()

            # Send mail here
            as2utils.senderrorreport(message, _(u'Failed to send message, error is %s' % e))

    """
    Receives a message from as2 and forwards the message to a QUARTET Server.
    The QU4RTET Server must be configured in the Routes. 
    """

    def receive(self, message):

        # Check if message has been processed and sent to a QU4RTET Server
        try:
            mr = MessageReceived.objects.get(message_id=message.message_id)
            if mr is not None and mr.processed:
                # Message has been processed so return
                return
        except MessageReceived.DoesNotExist:
            # Message no found, so it has not been processed, just continue
            pass
        except Exception as e:
            raise e

        payload = models.Payload.objects.get(id=message.payload_id)
        file = payload.file
        route = Routes.objects.get(partner__as2_name=message.partner.as2_name)
        print("Send to {0}".format(route.url))

        try:
            file_name = os.path.basename(file)
            files = {'file': (file_name, open(file, 'rb'))}
            resp = requests.post(route.url, auth=(route.username, route.password), files=files)
            print(resp.content)
            # Mark the message as processed
            MessageReceived.objects.create(message_id=message.message_id, processed=True)
        except Exception as e:
            raise e


"""
    Listens for pyAS2 Message Save.
"""


@receiver(post_save, sender=models.Message)
def handle_payload(sender, instance, created, **kwargs):
    # Don't route Outbound Messages
    if instance and instance.direction == 'OUT': return
    # If this is a create, then return - the payload hasn't been updated
    if created: return
    # if the payload is none, then return - the recieve() method will fail
    if instance.payload is None: return
    # Send to receive
    RouteFiles().receive(instance)
