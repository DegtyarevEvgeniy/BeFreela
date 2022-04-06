from django import forms
from django.forms import ModelChoiceField
from .models import *


class ProductCreationForm(forms.Form):
    product_name = forms.CharField(required=True)
    cost = forms.CharField(required=True)
    availability = forms.ChoiceField()
    description = forms.CharField()
    picture = forms.ImageField()


class addTasks(forms.Form):
    task_name = forms.CharField(label='Название', required=True, widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    select = forms.ModelChoiceField(
        queryset=Tag.objects.values_list("tag_name", flat=True).distinct(),
        empty_label=None
    )
    description = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'placeholder': 'Описание'}))
    price = forms.IntegerField(label='Цена', required=True, widget=forms.TextInput(attrs={'placeholder': 'Цена'}))
    data = forms.DateField(label='Дата', widget=forms.TextInput(attrs={'placeholder': 'Дата'}))
