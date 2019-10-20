from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('getdata/', views.getdata, name='getdata'),
    path('shelter/', views.shelter, name='shelter'),
]