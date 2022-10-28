from django.urls import path, register_converter
from rest_framework import routers
from . import views
from .converter import StringConverter

register_converter(StringConverter, 'urls')

urlpatterns = [
    path('<urls:key>/', views.index),


]