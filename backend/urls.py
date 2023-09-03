from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("base.urls")),
    path("api/admin/", include("core.urls")),
    path("api/auth/", include("accounts.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
