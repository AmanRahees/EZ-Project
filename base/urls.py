from django.urls import path
from .views import *

urlpatterns = [
    path('files', FilesAPI.as_view()),
    path('files/<int:id>', FileDownloadAPI.as_view()),
]