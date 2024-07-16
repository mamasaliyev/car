from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.users.views import UserAPIViewSet

from config import settings
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'users', UserAPIViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('users/', include('apps.users.urls')),
]
urlpatterns += doc_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
