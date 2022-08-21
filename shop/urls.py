from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='Shop Home'),
    path('about', views.about , name='about'),
    path('contact', views.contact , name='contact'),
    path('tracker', views.tracker , name='tracker'),
    path('search', views.search , name='search'),
    path('product', views.product , name='product'),
    path('checkout', views.checkout , name='checkout'),


]
