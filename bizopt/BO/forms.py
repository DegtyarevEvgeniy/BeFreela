from django import forms


class UserForm(forms.Form):
    login = forms.CharField(label='login', required=True, help_text="Логин")
    password = forms.CharField(label='password1', required=True, help_text="Пароль")
    sug_password = forms.CharField(label='password2', required=True, help_text="Подтвердите пароль")
    phone = forms.Integer(max_length=20, help_text="Телефон")
    name = forms.CharField(max_length=20, help_text="Имя")
    surname = forms.CharField(max_length=30, help_text="Фамилия")
    city = forms.CharField(max_length=20, help_text="Город")
