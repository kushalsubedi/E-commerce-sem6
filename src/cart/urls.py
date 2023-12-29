
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path("add_to_cart/<int:pk>", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),


]
