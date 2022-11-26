from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('login', views.login_user, name="login"),
    path('register', views.register, name="register"),
    path('register-product', views.ProductView.as_view(), name="product_register"),
    path('sell', views.sell, name="sell"),
]
