from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from .models import *
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput
        (attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput
        (attrs={'class':'form-control','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
        }


    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError('This field is required.')
        else:
            return email

class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']

# class PassChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(widget=forms.PasswordInput
#         (attrs={'class':'form-control','placeholder':'Enter Old Password'}))
#     new_password1 = forms.CharField(widget=forms.PasswordInput
#         (attrs={'class':'form-control','placeholder':'Enter New Password'}))
#     new_password2 = forms.CharField(widget=forms.PasswordInput
#         (attrs={'class':'form-control','placeholder':'Confirm Password'}))

# class PassResetForm(PasswordResetForm):
#     email = forms.CharField(widget=forms.EmailInput
#         (attrs={'class':'form-control', 'placeholder':'Enter ypur Email Id'}))

# class SetNewPassForm(SetPasswordForm):
#     new_password1 = forms.CharField(widget=forms.PasswordInput
#         (attrs={'class':'form-control','placeholder':'Enter new password'}))
#     new_passwrod2 = forms.CharField(widget=forms.PasswordInput
#         (attrs={'class':'form-comtrol','placeholder':'Confirm Password'}))


# Set New Password
class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Old Password'}))
    new_password1 =forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))
    new_password2 =forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Re-New Password'}))


# Password Reset TextBox With Registred E-Mail
class PassResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Registered E-Mail'}))
    
# New Password Set Registred E-Mail Link
class SetNewPassForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput
    (attrs={'class':'form-control','placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput
    (attrs={'class':'form-control','placeholder':'Confirm New Password'}))


class UserProfileChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter lastname'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email'}),
        }

class CustomeraddressForm(forms.ModelForm):
    class Meta:
        model = CustomeraddressModel
        fields = ['fname','lname','email','mobile','country','state','city','pincode','add1','add2']
        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Firstname'}),
            'lname': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Lastname'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email_id'}),
            'mobile': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mobile_no'}),
            'country': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter country'}),
            'state': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}),
            'pincode':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Pincode'}),
            'add1': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address 1'}),
            'add2': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address 2'}),
        }


