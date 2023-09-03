from django.urls import path
from .views import *

urlpatterns = [
    path('login', AdminLoginAPI.as_view()),
    path('file/upload', FilesAPI.as_view()),
]