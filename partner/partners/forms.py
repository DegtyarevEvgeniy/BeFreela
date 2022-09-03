from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from partners.models import Partner


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # tab 1

        self.fields['email'].label='Почта'
        self.fields['email'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
        })
        self.fields['password1'].label='Пароль'
        self.fields['password1'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'minlength': '1'
        })

        self.fields['city'].label = 'Город'
        self.fields['city'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'city',
            'id': 'city',
            'type': 'text',
            'minlength': '1'
        })
        self.fields['password2'].label='Повторите пароль'
        self.fields['password2'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'minlength': '1'
        })
        self.fields['first_name'].label='Имя'
        self.fields['first_name'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'first_name',
            'id': 'first_name',
            'type': 'text',
            'minlength': '1'
        })
        self.fields['last_name'].label='Фамилия'
        self.fields['last_name'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'last_name',
            'id': 'last_name',
            'type': 'text',
            'minlength': '1'
        })
        # tab 2
        self.fields['ogrn'].label='ОГРН'
        self.fields['ogrn'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'ogrn',
            'id': 'ogrn',
            'type': 'number',
            'value': '',
            'placeholder': 'Введите свой ОГРН',
            'minlength': '1'
        })
        self.fields['inn'].label='ИНН'
        self.fields['inn'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'inn',
            'id': 'inn',
            'type': 'number',
            'value': '',
            'placeholder': 'Введите свой ИНН',
            'minlength': '1'
        })
        self.fields['kpp'].label='КПП'
        self.fields['kpp'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'kpp',
            'id': 'kpp',
            'type': 'number',
            'value': '',
            'placeholder': 'Введите свой КПП',
            'minlength': '1'
        })
        self.fields['street'].label='Адрес регистрации с почтовым индексом'
        self.fields['street'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'street',
            'id': 'street',
            'type': 'text',
            'placeholder': '162390, Россия, Вологодская область, город Великий Устюг, дом Деда Мороза',
            'minlength': '1'
        })
        self.fields['fiz_adress'].label='Физический адрес'
        self.fields['fiz_adress'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'fiz_adress',
            'id': 'fiz_adress',
            'type': 'text',
            'placeholder': 'Мурманская обл., Мончегорск, Лапландский заповедник, пер.Зеленый, д.8',
            'minlength': '1'
        })
        self.fields['index'].label='Индекс'
        self.fields['index'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'index',
            'id': 'index',
            'type': 'number',
            'value': '',
            'placeholder': '184506',
            'minlength': '1'
        })
        self.fields['name_small'].label='Краткое наименование'
        self.fields['name_small'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'name_small',
            'id': 'name_small',
            'type': 'text',
            'placeholder': '',
            'minlength': '1'
        })
        self.fields['nameFull'].label='Полное наименование'
        self.fields['nameFull'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'nameFull',
            'id': 'nameFull',
            'type': 'text',
            'placeholder': '',
            'minlength': '1'
        })
        # tab 3
        self.fields['korr_check'].label='Корреспондентский счет'
        self.fields['korr_check'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'korr_check',
            'id': 'korr_check',
            'type': 'number',
            'value': '',
            'placeholder': '',
            'minlength': '1'
        })
        self.fields['payment_account'].label='Расчетный счет'
        self.fields['payment_account'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'payment_account',
            'id': 'payment_account',
            'type': 'number',
            'value': '',
            'placeholder': '',
            'minlength': '1'
        })
        self.fields['bik'].label='БИК'
        self.fields['bik'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'bik',
            'id': 'bik',
            'type': 'number',
            'value': '',
            'placeholder': '',
            'minlength': '1'
        })
        self.fields['reg_form'].label='Форма регистрации'
        self.fields['reg_form'].widget.attrs.update({
            'class': 'uk-input',
            'required': '',
            'name': 'reg_form',
            'id': 'reg_form',
            'type': 'text',
            'placeholder': '',
            'minlength': '1'
        })
        # tab 4
        self.fields['checking_account'].label = 'Код'
        self.fields['checking_account'].widget.attrs.update({
            'class': 'uk-input',
            'required': 'none',
            'name': 'checking_account',
            'id': 'checking_account',
            'type': 'number',
            'value': '',
            'minlength': '1'
        })
    class Meta:
        model = Partner
        fields = ('email', 'city', 'first_name', 'last_name', 'email',
        'ogrn', 'inn', 'kpp', 'street', 'fiz_adress', 'index', 'checking_account', 'bik', 
        'korr_check','name_small','nameFull', 'payment_account', 'reg_form')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Partner
        fields = ( 'email',  'city', 'first_name', 'last_name')
