from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import CustomUser
from accounts.serializers import RegisterUserSerializers
from accounts.verify import send_otp

# Create your views here.

class RegisterAPI(APIView):
    permission_classes =  [AllowAny]
    def post(self, request):
        serializer = RegisterUserSerializers(data=request.data)
        if serializer.is_valid():
            user =  serializer.save()
            otp = send_otp(request, user.email)
            user.otp = otp
            user.save()
            message = 'User registered successfully. Please check your Email to verify your Account.'
            return Response({'message': message},status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class VerifyAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            email = request.data.get('email')
            otp = request.data.get('otp')
            user = CustomUser.objects.get(email=email)
            if user.otp == otp:
                user.is_active = True
                user.save()
                return Response({'message': 'Email Verified Successfully!'}, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'Invalid OTP!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'Error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)
        
    
class LoginAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active == True:
                refresh_token = RefreshToken.for_user(user)
                access_token = str(refresh_token.access_token)
                refresh_token = str(refresh_token)
                return Response({'access': access_token, 'refresh': refresh_token}, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'Your Account is not Verified!'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'Error': 'Invalid Credentials!'}, status=status.HTTP_401_UNAUTHORIZED)
        
class TokenRefreshAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        refresh = request.data.get("refresh")
        if refresh:
            try:
                refresh_obj = RefreshToken(refresh)
                access_token = str(refresh_obj.access_token)
                return Response({"access": access_token}, status=status.HTTP_200_OK)
            except:
                return Response({"Error": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)