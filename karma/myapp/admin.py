from django.contrib import admin
from .models import Product, Categories, Cart , CustomeraddressModel, Order
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["Description", "price", "name", "img", "category"]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["quantity", "product", "user"]


@admin.register(CustomeraddressModel)
class CustomeraddressModelAdmin(admin.ModelAdmin):
    list_display = ["user", "lname", "fname", "email"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "product","status",  "customer","quantity")
