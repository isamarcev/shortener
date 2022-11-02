from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shortener import settings


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include('api_shortener.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [path('admin/', admin.site.urls)]

