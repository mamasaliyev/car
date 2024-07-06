from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # boshqa yo'llar bu yerga qo'shiladi
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
