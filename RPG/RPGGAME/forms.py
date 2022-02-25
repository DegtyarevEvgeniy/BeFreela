from django import forms

class PersForm(forms.Form):
    name =  forms.CharField (label='Имячко', max_length=20, required=True)
    desc =  forms.CharField(label='Описание', max_length=200, required=False)
    age  =  forms.IntegerField(label='Возраст', min_value=14, max_value=99, required=True)