from django.urls import path, register_converter
from . import views
from .converter import StringConverter

register_converter(StringConverter, 'urls')

urlpatterns = [
    path('<urls:key>/', views.index),
    path('api/shorter/', views.ShortUrlViewSet.as_view()),
]