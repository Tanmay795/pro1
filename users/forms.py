from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField(max_length=100)

    class Meta:
        model= User
        fields=['username','email','address','password1','password2']
