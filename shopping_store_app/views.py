from django.shortcuts import render, redirect
from .models import Product, Customer
from .serializer import CustomerSerializer, ProductSerializer
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .forms import CustomerForm, AddressForm


def base_list(request):
    form = CustomerForm
    add = AddressForm

    if request.method == "POST":
        form = CustomerForm(request.POST)
        add = AddressForm(request.POST)
        if form.is_valid and add.is_valid():
            form.save()
            add.save()
            return redirect("customer.html")

    context = {"form": form, "add": add}

    return render(request, "shopping_store_app/base.html", context)


def products_list(request):
    products = Product.objects.all().order_by("price")
    context = {"Products": products}
    return render(request, "shopping_store_app/product.html", context)


def customers_list(request):
    users = Customer.objects.all().order_by("date_created")
    context = {"Users": users}
    return render(request, "shopping_store_app/customer.html", context)


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name", "last_name"]
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ["first_name", "last_name"]


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ["price", "default_currency"]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
