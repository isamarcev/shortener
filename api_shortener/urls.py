from django.urls import path, register_converter
from . import views
from .converter import StringConverter

register_converter(StringConverter, 'urls')

urlpatterns = [
    path('', views.redirect, name='start_page'),
    path('<urls:key>/', views.redirect),
    path('api/shorter/', views.ShortUrlViewSet.as_view()),
]
