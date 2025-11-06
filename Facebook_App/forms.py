from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FacebookPost


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)


# class Meta:
#     model = User
#     fields = ["username","email","password1","password2"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = FacebookPost
        fields = ['text_area', 'image']