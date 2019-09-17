from django.contrib import admin
from models import Routes, MessageReceived

from django.contrib import admin
from as2 import forms
from as2 import models
import os


class PrivateCertificateAdmin(admin.ModelAdmin):
    form = forms.PrivateCertificateForm
    list_display = ('__str__', 'download_link',)

    def download_link(self, obj):
        return '<a href="/as2/certificates/' + os.path.basename(
            obj.certificate.name) + '">' + 'Click Here' + '</a>'

    download_link.allow_tags = True
    download_link.short_description = "Download Link"


class PublicCertificateAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'download_link',)

    def download_link(self, obj):
        return '<a href="/as2/certificates/' + os.path.basename(
            obj.certificate.name) + '">' + 'Click Here' + '</a>'

    download_link.allow_tags = True
    download_link.short_description = "Download Link"


class PartnerAdmin(admin.ModelAdmin):
    form = forms.PartnerForm
    list_display = ['name', 'as2_name', 'target_url', 'encryption', 'encryption_key', 'signature', 'signature_key',
                    'mdn', 'mdn_mode']
    list_filter = ('name', 'as2_name')
    fieldsets = (
        (None, {
            'fields': (
                'name', 'as2_name', 'email_address', 'target_url', 'subject', 'content_type', 'confirmation_message')
        }),
        ('Http Authentication', {
            'classes': ('collapse', 'wide'),
            'fields': ('http_auth', 'http_auth_user', 'http_auth_pass', 'https_ca_cert')
        }),
        ('Security Settings', {
            'classes': ('collapse', 'wide'),
            'fields': ('compress', 'encryption', 'encryption_key', 'signature', 'signature_key')
        }),
        ('MDN Settings', {
            'classes': ('collapse', 'wide'),
            'fields': ('mdn', 'mdn_mode', 'mdn_sign')
        }),
        ('Advanced Settings', {
            'classes': ('collapse', 'wide'),
            'fields': ('keep_filename', 'cmd_send', 'cmd_receive')
        }),
    )

class RoutesAdmin(admin.ModelAdmin):
    fields = ('name', 'partner', 'url', 'username', 'password' )
    class Meta:
        model = Routes

class MessageReceivedAdmin(admin.ModelAdmin):
     fields = ('message_id', 'processed' )
     list_display = ('message_id', 'processed')
     class Meta:
         model = MessageReceived


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'as2_name']
    list_filter = ('name', 'as2_name')


admin.site.register(models.PrivateCertificate, PrivateCertificateAdmin)
admin.site.register(models.PublicCertificate, PublicCertificateAdmin)
admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.Partner, PartnerAdmin)
admin.site.register(models.Message)
admin.site.register(models.MDN)




admin.site.register(Routes, RoutesAdmin)
admin.site.register(MessageReceived, MessageReceivedAdmin)