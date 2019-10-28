from rest_framework import serializers
from .models import QuartetFileUpload


class QuartetFileUploadSerializer(serializers.ModelSerializer):


    class Meta():
        model = QuartetFileUpload
        fields = ('file', 'organization', 'partner', 'uploaded_at')
