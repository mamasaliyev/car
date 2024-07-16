from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.users.views import UserAPIViewSet

from config import settings
from .yasg import urlpatterns as doc_urls

from apps.catalog.views import LogoViewSet, CarViewSet, ContractViewSet

router = routers.DefaultRouter()
router.register(r'users', UserAPIViewSet, basename='users')
router.register(r'logos', LogoViewSet)
router.register(r'cars', CarViewSet)
router.register(r'contracts', ContractViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('users/', include('apps.users.urls')),
    path('catalog/', include('apps.catalog.urls'))
]
urlpatterns += doc_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
