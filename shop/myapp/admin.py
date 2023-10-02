from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(user)
admin.site.register(Contact)
admin.site.register(Add_product)
admin.site.register(Add_to_cart)
admin.site.register(main_category)