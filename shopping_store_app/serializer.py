from dataclasses import field
from rest_framework import serializers
from shopping_store_app.models import Customer, Product
from djmoney.contrib.django_rest_framework import MoneyField


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
