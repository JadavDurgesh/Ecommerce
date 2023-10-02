
from django.contrib import admin
from django.urls import path
from myapp.form import PassResetForm,SetNewPassForm
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import AboutView, Add_to_cartView, Add_to_wishlistView, AddressDeleteView, AllproductView, ChangePassView, CheckoutView, CustomerAddressView, DeleteView, DeletewishlistView, LogoutView, OrderView, ProfileView, SearchView, SigninView, UpdateaddressView, WishListView, clearcart, contactview, homeview, minus_quantity, pluse_quantity, signupview ,ProductInfoView, CartView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeview,name='home'),
    path('signup/',signupview),
    path('signin/',SigninView, name='login'),
    path('out/',LogoutView),
    path('passchange/',ChangePassView),
    path('profile/',ProfileView),
    path('proinfo/<int:id>/',ProductInfoView),
    path('allproducts/',AllproductView),
    path('cart/', CartView, name='cart'),
    path('addtocart/<int:id>/',Add_to_cartView),
    path('deletecart/<int:id>/',DeleteView),
    path('pluscart/<int:id>/',pluse_quantity),
    path('minuscart/<int:id>/',minus_quantity),
    path('clearcart/',clearcart),
    path('wish/<int:id>/',Add_to_wishlistView),
    path('wishlist/',WishListView),
    path('deletewishlist/<int:id>/',DeletewishlistView),

    path('address/', CustomerAddressView,name='address'),
    path('Addressdelete/<int:id>/',AddressDeleteView,name='Addressdelete'),
    path('Addressupdate/<int:id>/',UpdateaddressView,name='Addressupdate'),
    path('orders/', OrderView,name='orders'),
    path('checkout/', CheckoutView,name='checkout'),
    path('contact/',contactview),

    path('searchview/', SearchView,name='searchview'),
    path('about/',AboutView),

     #Password Reset
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=PassResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=SetNewPassForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
    




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

