from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Customer, Product, Address, Payment


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "your_email"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
