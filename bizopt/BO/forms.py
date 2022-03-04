from django import forms


class UserForm(forms.Form):
    login = forms.CharField(label='login', required=True, help_text="Логин", widget=forms.TextInput(attrs={'placeholder':'Логин'}))
    password = forms.CharField(label='password1', required=True, help_text="Пароль", widget=forms.TextInput(attrs={'placeholder':'Пароль'}))
    sug_password = forms.CharField(label='password2', required=True, help_text="Подтвердите пароль", widget=forms.TextInput(attrs={'placeholder':'Подтвердите пароль'}))
    phone = forms.IntegerField(help_text="Телефон", widget=forms.TextInput(attrs={'placeholder':'Телефон'}))
    name = forms.CharField(max_length=20, help_text="Имя", widget=forms.TextInput(attrs={'placeholder':'Имя'}))
    surname = forms.CharField(max_length=30, help_text="Фамилия", widget=forms.TextInput(attrs={'placeholder':'Фамилия'}))
    city = forms.CharField(max_length=20, help_text="Город", widget=forms.TextInput(attrs={'placeholder':'Город'}))
    email = forms.CharField(max_length=20, help_text="Почта", widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
