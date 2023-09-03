from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from core.models import FileUploads
from base.serializers import FileSerializers

# Create your views here.

class FilesAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        files = FileUploads.objects.all()
        serializer = FileSerializers(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FileDownloadAPI(APIView):
    def get(self, request, id):
        try:
            file = FileUploads.objects.get(pk=id)
            serializer = FileSerializers(file, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "File not Found!"}, status=status.HTTP_404_NOT_FOUND)