from django.db import models
from django.utils.translation import ugettext as _
from pyas2.models import Partner


class InboundFiles(models.Model):
    file = models.FileField(blank=False, null=False, upload_to='uploads/')
    sender = models.CharField(max_length=255, null=True)
    receiver = models.CharField(max_length=255, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        app_label = 'as2'


class Routes(models.Model):
    name = models.CharField(_('Name'), max_length=255, help_text=_('Name of the Route'))
    url = models.CharField(_('QU4RTET URL'),
                           max_length=255)

    partner = models.ForeignKey(Partner)
    username = models.CharField(_('Username'),
                                max_length=255)

    password = models.CharField(_('Password'),
                                max_length=255)

    class Meta:
        app_label = 'as2'

    def __str__(self):
        return self.name

class MessageReceived(models.Model):
    message_id = models.CharField(_('Message Id'), max_length=255, help_text=_('Id of a Message Recieved'))
    processed = models.BooleanField(_('Processed'),
                           default=False)


    class Meta:
        app_label = 'as2'

    def __str__(self):
        return self.message_id
