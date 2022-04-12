from django import forms
from django.forms import ModelChoiceField

from django.forms import ModelForm, TextInput, Textarea, Select, CharField
from .models import *


COUNTRY_CHOICE = [
    ('Afghanistan', 'Afghanistan'),
    ('Aland Islands', 'Åland Islands'),
    ('Albania', 'Albania'),
    ('Algeria', 'Algeria'),
]

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product_creator
        fields = '__all__'
        widgets = {
            'product_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "name",
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
            }),
            'country': Select(attrs={
                'class': 'input-group mt-2 mb-2',
            }, choices=COUNTRY_CHOICE),

            'brand': TextInput(attrs={
                'class': 'form-control',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
            }),
            'width_product': TextInput(attrs={
                'class': 'form-control',
            }),
            'height_product': TextInput(attrs={
                'class': 'form-control',
            }),
            'length_product': TextInput(attrs={
                'class': 'form-control',
            }),
            'width_packaging': TextInput(attrs={
                'class': 'form-control',
            }),
            'height_packaging': TextInput(attrs={
                'class': 'form-control',
            }),
            'length_packaging': TextInput(attrs={
                'class': 'form-control',
            }),

        }

    # product_name = forms.CharField(required=True)
    # cost = forms.CharField(required=True)
    # availability = forms.ChoiceField()
    # description = forms.CharField()
    # picture = forms.ImageField()



class MyProfile(forms.Form):
    select = forms.ModelChoiceField(
        queryset=Tag.objects.values_list("tag_name", flat=True).distinct(),
        empty_label=None
    )


class addTasks(forms.Form):
    task_name = forms.CharField(label='Название', required=True, widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    select = forms.ModelChoiceField(
        queryset=Tag.objects.values_list("tag_name", flat=True).distinct(),
        empty_label=None
    )
    description = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'placeholder': 'Описание'}))
    price = forms.IntegerField(label='Цена', required=True, widget=forms.TextInput(attrs={'placeholder': 'Цена'}))
    data = forms.DateField(label='Дата', widget=forms.TextInput(attrs={'placeholder': 'Дата'}))
