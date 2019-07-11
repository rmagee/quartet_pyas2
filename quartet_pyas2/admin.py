from django.contrib import admin
from models import Routes, MessageReceived
class RoutesAdmin(admin.ModelAdmin):
    fields = ('name', 'partner', 'url', 'username', 'password' )
    class Meta:
        model = Routes

class MessageReceivedAdmin(admin.ModelAdmin):
     fields = ('message_id', 'processed' )
     list_display = ('message_id', 'processed')
     class Meta:
         model = MessageReceived

admin.site.register(Routes, RoutesAdmin)
admin.site.register(MessageReceived, MessageReceivedAdmin)