from django import forms
from django.forms import ModelChoiceField

from django.forms import ModelForm, TextInput, Textarea, Select, CharField
from .models import *
from taggit.models import Tag

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
        queryset=Tag.objects.all(),
        empty_label=None
    )


class addTasks(forms.Form):
    task_name = forms.CharField(label='Название', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название',
        'id': "floatingInputGrid",
    }))

    select = forms.ModelChoiceField(queryset=Tag.objects.all(), widget =forms.Select(attrs = {
        'class': "form-select",
    }))


    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Описание',
        'style': "height: 100px",
        'id': "floatingTextarea2",

    }))
    price = forms.IntegerField(label='Цена', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Цена',
    }))
    date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))


class Resume(forms.Form):
    description = forms.CharField(label='Расскажите о себе', required=True, widget=forms.Textarea(attrs={
        'class': "form-control",
    }))
    is_company = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': "form-check-input",
        'onchange': "isCompany()",
        'id': "isCompanyTrigger",
    }))
    company_name = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Название компании",

    }))
    email = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "form-control",
    }))
    first_name = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "form-control",
    }))
    cover = forms.ImageField(required=False)
    telegram = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "@tag",
    }))
    vk = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "https://vk.com/yourid",
    }))
    whatsapp = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "+71234567890",
    }))
    instagram = forms.CharField(label='Расскажите о себе', required=False, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': " https://instagram.com/tag",
    }))
    tag = forms.CharField(label='Расскажите о себе', required=True, widget=forms.TextInput(attrs={
        'class': "form-control",
    }))
    published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': "form-check-input",
        'value': "1",
    }))