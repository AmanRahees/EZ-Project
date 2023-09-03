from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from core.models import FileUploads
from core.serializers import FileUploadSerializers

# Create your views here.

class AdminLoginAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_superadmin == True:
                refresh_token = RefreshToken.for_user(user)
                access_token = str(refresh_token.access_token)
                refresh_token = str(refresh_token)
                return Response({'access': access_token, 'refresh': refresh_token}, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'Error': 'Invalid Credentials!'}, status=status.HTTP_401_UNAUTHORIZED)

class FilesAPI(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        data = request.data
        serializer = FileUploadSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "File Upload Successfully!"}, status=status.HTTP_200_OK)
        return Response({"Error": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)