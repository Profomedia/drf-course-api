from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductView, name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView, name='product-detail'),
]
