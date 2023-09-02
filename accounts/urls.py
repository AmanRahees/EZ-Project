from django.urls import path
from .views import *

urlpatterns = [
    path("register", RegisterAPI.as_view()),
    path("login", LoginAPI.as_view()),
    path("otp/verify", VerifyAPI.as_view()),
    path("token/refresh", TokenRefreshAPI.as_view()),
]