from django.urls import path, include
from .views import products_list
from shopping_store_app import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers, serializers, viewsets
from .views import CustomerListView, ProductListView


urlpatterns = [
    path("", views.base_list, name="main"),
    path("products/", views.products_list, name="products"),
    path("customers/", views.customers_list, name="customer"),
    path("customers-list/", views.CustomerListView.as_view(), name="customers-list"),
    path(
        "customers-list/<int:pk>", views.CustomerDetailView.as_view(), name="customer"
    ),
    path("products-list/", views.ProductListView.as_view(), name="products-list"),
    path("products-list/<int:pk>", views.ProductDetailView.as_view(), name="product"),
]
