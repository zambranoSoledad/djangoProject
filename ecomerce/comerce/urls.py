from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name="home"),
    path('contact', views.contact, name="contact"),
    path('login', views.login_user, name="login"),
    path('logout', LogoutView.as_view(template_name="index.html"), name="logout"),
    path('register', views.register, name="register"),
    path('register-product', views.ProductView.as_view(), name="product_register"),
    path('sell/<int:id_producto>', views.sell, name="sell"),
    path('sell/confirm', views.confirm_sell, name="confirm_sell"),
]
