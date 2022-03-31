from django.contrib import admin
from .models import Payment, Address, Customer, Product

admin.site.header = "LOGIN TO DEVELOPER IVAN"
admin.site.site_header = "MY E-SHOP DASHBOARD"
admin.site.index_title = "WELCOME TO YOUR ADMIN DASHBOARD"


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "delivery_address")
    list_filter = ("last_name", "first_name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_category", "quantity", "size", "price")
    list_filter = ("price", "product_category")


admin.site.register(Address)
admin.site.register(Payment)
