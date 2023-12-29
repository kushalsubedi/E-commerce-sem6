from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_Product, name='create'),
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('update_product/<int:pk>', views.update_product, name='update_product'),
    path('delete_product/<int:pk>', views.delete_product, name='delete_product'),
    path('create_category/', views.create_category, name='category'),
    # ]
]
