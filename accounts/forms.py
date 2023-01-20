from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=11, help_text='09123456789')

    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2", "phone", ]
