from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext , gettext_lazy  as _
from django.contrib.auth import password_validation
from .models import Customer




class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required = True, widget = forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(required = True, widget = forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label = _('Password'), strip = False,
    widget = forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))



class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label = _("Email"),max_length = 254,
     widget = forms.EmailInput(attrs = {'autocomplete':'email',
     'class':'form-control'}))


class MysSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label = ("New Password"),
    strip = False, widget = forms.PasswordInput(attrs=
    {'autocomplete':'new-password','class':'form-control'}),
    help_text = password_validation.
    password_validators_help_text_html())

    new_password2 = forms.CharField(label = ("Confirm New Password"),
    strip = False, widget = forms.PasswordInput(attrs=
    {'autocomplete':'new-password','class':'form-control'}))



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =['first_name','last_name','Contact_No','locality','city','state','zipcode']
        widgets = {'first_name':forms.TextInput(attrs = {'class':'form-control'}),
                  'last_name':forms.TextInput(attrs ={'class':'form-control'}),
                  'Contact_No':forms.NumberInput(attrs={'class':'form-control'}),
                 'locality':forms.TextInput(attrs = {'class':'form-control'}),
                  'city':forms.TextInput(attrs = {'class':'form-control'}),
                  'state':forms.Select(attrs = {'class':'form-control'}),
                  'zippcode':forms.NumberInput(attrs = {'class':'formcontrol'})}
