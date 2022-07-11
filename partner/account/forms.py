from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import Account
from django.contrib.auth.models import User
from django.forms import Select

COUNTRY_CHOICE = [
    ('Russia','Belarus'),
    ('Kazakhstan','Kyrgyzstan'),
    ('Armenia') ,
]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('country', 'inn', 'provider', 'fio', 'ogrnip')
        widgets = {'country': Select(attrs={
            'class': 'input-group mt-2 mb-2',
        }, choices=COUNTRY_CHOICE),
        }




class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('country', 'inn', 'provider', 'fio', 'ogrnip')
        widgets = {'country': Select(attrs={
                    'class': 'input-group mt-2 mb-2',
                }, choices=COUNTRY_CHOICE),
        }