from django.urls import path, register_converter
from . import views
from .converter import StringConverter

register_converter(StringConverter, 'urls')

urlpatterns = [
    path('', views.MainPageView.as_view(), name='start_page'),
    path('<urls:key>/', views.redirect, name='redirect'),
    path('api/shorter/', views.ShortUrlViewSet.as_view(), name='shortener'),
]
