from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from . import models

class LoginForm(AuthenticationForm):
    username = UsernameField(label="Username", widget=forms.TextInput(attrs={'autofocus':'True', "class": "form-control",}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'autocomplete':'current-password', "class": "form-control",}))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'autofocus':'True', "class": "form-control",}))
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'autofocus':'True', "class": "form-control",}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'autofocus':'True', "class": "form-control",}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'autofocus':'True', "class": "form-control",}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class MyPaswordResetForm(PasswordChangeForm):
    pass

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ('name', 'locality', 'city','mobile')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={"class": "form-control",}),
            'city': forms.Select(attrs={"class": "form-control",}),
            'mobile': forms.NumberInput(attrs={"class": "form-control", }),
            
        }