from django.contrib import admin
from .models import Maincategory, contactmodel,productmodel, Cart,Wishlist, CustomeraddressModel, Order
# Register your models here.


@admin.register(Maincategory)
class MaincategoryAdmin(admin.ModelAdmin):
    list_display = ("name","image")




@admin.register(productmodel)
class productmodelAdmin(admin.ModelAdmin):
    list_display =  ["sell_price", "discount_price", "discount", "og_price", "image", "name", "pcate"]





@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["quantity", "product", "user"][::-1]


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ["quantity", "product", "user"][::-1]



@admin.register(CustomeraddressModel)
class CustomeraddressModelAdmin(admin.ModelAdmin):
    list_display = ("add2", "add1", "pincode", "city", "state", "counrty", "mobile", "email", "lname", "fname", "user")



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["status", "order_date", "quantity", "product", "customer", "user"][::-1]




@admin.register(contactmodel)
class contactAdmin(admin.ModelAdmin):
    list_display = ["message", "subject", "email", "name", "user"][::-1]