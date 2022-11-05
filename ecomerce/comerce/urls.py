from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('register', views.register, name="register"),
    path('link', views.link, name="link"),
    path('sell', views.sell, name="sell"),
]
