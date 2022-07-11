from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import Account


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'phone', 'city', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'phone', 'city', 'first_name', 'last_name')
