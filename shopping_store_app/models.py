from tabnanny import verbose
from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField


class Payment(models.Model):
    cc_number = CardNumberField(("card number"))
    cc_expiry = CardExpiryField(("expiration date"))
    cc_code = SecurityCodeField(("security code"))

    def __str__(self):
        return self.cc_number

    def check_len_and_first_digit(self):
        if len(self.cc_number) == 16:
            return True
        elif self.cc_number[0] == "4" or "5" or "6":
            return True
        else:
            return False

    class Meta:
        verbose_name_plural = "CREDIT CARDS"


class Address(models.Model):
    street = models.TextField(max_length=250)
    zip_code = models.TextField(blank=False, default=1000)
    city = models.TextField(max_length=100)
    country = CountryField()

    def __str__(self):
        return str(self.street) + " " + str(self.city)

    class Meta:
        verbose_name_plural = "DELIVERY ADDRESS"


class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    your_email = models.EmailField(null=True, blank=True)
    credit_card = models.ForeignKey(
        Payment, null=True, blank=True, on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)
    delivery_address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name + str(self.delivery_address)

    class Meta:
        verbose_name = "Customers"
        verbose_name_plural = "CUSTOMERS"


class Product(models.Model):

    category = [
        ("__", "---------"),
        ("TS", "Tracksuits"),
        ("PJ", "Pajamas"),
        ("BL", "Blouses"),
    ]

    sizes_product = [
        ("Small", "S"),
        ("Medium", "M"),
        ("Large", "L"),
        ("Extra_Large", "XL"),
    ]

    name = models.CharField(
        null=False,
        blank=False,
        max_length=250,
    )
    product_category = models.CharField(
        max_length=250,
        choices=category,
        default="---------",
    )
    quantity = models.PositiveIntegerField(default=0)
    size = models.CharField(choices=sizes_product, default="S", max_length=250)
    price = MoneyField(max_digits=14, decimal_places=1, default_currency="USD")

    def __str__(self):
        return str(self.name) + " - " + str(self.price)

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "PRODUCTS"
