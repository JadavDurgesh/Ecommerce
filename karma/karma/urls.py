
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.form import PassResetForm,SetNewPassForm
from myapp.views import * 
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('signup/',signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('passwordchange/', passwordchange, name='passwordchange'),
    path('profile/', profile, name='profile'),
    path('address/', address, name='address'),
    path('addressupdate/<int:id>/', addressupdate, name='addressupdate'),
    path('addressdelete/<int:id>/', addressdelete, name='addressdelete'),
    path('singleblog/', singleblog, name='singleblog'),
    path('cart/', cart, name='cart'),
    path('addtocart/<int:id>/',addtocart,name='addtocart'),
    path('plusquantity/<int:id>/',plusquantity,name='plusquantity'),
    path('minusquantity/<int:id>/',minusquantity,name='minusquantity'),
    path('deleteitem/<int:id>/',deleteitem,name='deleteitem'),
    path('category/', category, name='category'),
    path('order/', order, name='order'),
    path('checkout/', checkout, name='checkout'),
    path('singleproduct/<int:id>/', singleproduct, name='singleproduct'),
    path('singleproduct/', singleproduct, name='singleproduct'),
    path('logout/',logout_user, name='logout'),
    path('track/',trac,name='track'),




    # path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=PassResetForm), name="password_reset"),
    # path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    # path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=SetNewPassForm), name="password_reset_confirm"),
    # path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),

    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=PassResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=SetNewPassForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
