from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList, name='product-list'),
    path('products/info/', views.Product_info, name='product-info'),
    path('products/<int:pk>/', views.ProductDetailView, name='product-detail'),
    path('orders/', views.order_list, name='order-list'),
    # path('orders/<int:pk>/', views.order_detail, name='order-detail'),
]
