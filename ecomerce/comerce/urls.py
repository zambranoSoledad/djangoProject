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
    path('product/add', views.ProductView.as_view(), name="product_register"),
    path('product/list', views.ProductTableView.as_view(), name="product_list"),
    path('message/list', views.MessageTableView.as_view(), name="message_list"),
    path('sell/<int:id_producto>', views.sell, name="sell"),
    path('sell/confirm', views.confirm_sell, name="confirm_sell"),
    path('sell/success', views.success_sell, name="success_sell"),
    path('sell/list', views.SellListView.as_view(), name="sell_list"),
    path('category/add', views.CategoryView.as_view(), name="category_register"),
    path('category/list', views.CategoryTableView.as_view(), name="category_list")
]
