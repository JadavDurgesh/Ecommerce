from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('product', views.product, name='product'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('checkout', views.checkout, name='checkout'),
    path('faq', views.faq, name='faq'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout',views.logout, name='logout'),
    path('forgetpassword',views.forgetpassword, name='forgetpassword'),
    path('newpassword',views.newpassword, name='newpassword'),
    path('add_to_cart/<int:id>',views.add_to_cart, name='add_to_cart'),
    path('minus/<int:id>',views.minus, name='minus'),
    path('plus/<int:id>',views.plus, name='plus'),
    path('remove/<int:id>',views.remove, name='remove'),
    path('blogdetails/<str:id>', views.blogdetails, name='blogdetails'),
    path('category/<str:id>', views.category, name='category')
        
    
]