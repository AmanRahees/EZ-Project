from rest_framework import serializers
from core.models import FileUploads

class FileUploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = FileUploads
        fields = ("name", "file")

    def validate_file(self, file):
        file_type = file.name.split('.')[-1].lower()
        allowed_types = ['pptx', 'docx', 'xlsx']
        if file_type in allowed_types:
            return file
        else:
            raise serializers.ValidationError("Invlaid File type!")