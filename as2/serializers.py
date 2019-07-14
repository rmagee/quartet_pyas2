from rest_framework import serializers
from .models import InboundFiles


class InboundFileSerializer(serializers.ModelSerializer):


    class Meta():
        model = InboundFiles
        fields = ('file', 'sender', 'receiver', 'uploaded_at')
