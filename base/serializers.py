from rest_framework import serializers
from core.models import FileUploads

class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = FileUploads
        fields = ("name", "file")