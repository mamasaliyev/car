from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.news_about.views import NewsAPIViewSet, AboutAPIViewSet
from apps.users.views import UserAPIViewSet

from config import settings
from .yasg import urlpatterns as doc_urls
from .views import HomePageView

from apps.catalog.views import LogoViewSet, CarViewSet, ContractViewSet

router = routers.DefaultRouter()
# users
router.register(r'users', UserAPIViewSet, basename='users')
# catalog
router.register(r'logos', LogoViewSet, basename='logos')
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'contracts', ContractViewSet, basename='contracts')
# news_about
router.register(r'News', NewsAPIViewSet, basename='news')
router.register(r'About', AboutAPIViewSet, basename='about')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', HomePageView.as_view(), name='home'),
    path('users/', include('apps.users.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('news_about/', include('apps.news_about.urls')),
]
urlpatterns += doc_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
