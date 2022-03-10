from django import forms


class UserForm(forms.Form):
    login = forms.CharField(label='login', required=True, help_text="Логин",
                            widget=forms.TextInput(attrs={'placeholder':'Логин'}))
    password = forms.CharField(label='password1', required=True, help_text="Пароль",
                               widget=forms.TextInput(attrs={'placeholder':'Пароль'}))
    sug_password = forms.CharField(label='password2', required=True, help_text="Подтвердите пароль",
                                   widget=forms.TextInput(attrs={'placeholder': 'Подтвердите пароль'}))
    phone = forms.IntegerField(help_text="Телефон",
                               widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    name = forms.CharField(max_length=20, help_text="Имя",
                           widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(max_length=30, help_text="Фамилия",
                              widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    city = forms.CharField(max_length=20, help_text="Город",
                           widget=forms.TextInput(attrs={'placeholder': 'Город'}))
    email = forms.CharField(max_length=20, help_text="Почта",
                            widget=forms.TextInput(attrs={'placeholder': 'Почта'}))


class UserLoginForm(forms.Forms):
    login = forms.CharField(label='login', required=True, help_text="Логин",
                            widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label='password1', required=True, help_text="Пароль",
                               widget=forms.TextInput(attrs={'placeholder': 'Пароль'}))


class OrdersCreators(forms.Form):
    desc = forms.CharField(label='desc', required=True, help_text="Описание",
                            widget=forms.TextInput(attrs={'placeholder': 'Описание'}))
    type = forms.CharField(label='type', required=True, help_text="Тип работы",
                            widget=forms.TextInput(attrs={'placeholder': 'Тип работы'}))
    time = forms.CharField(label='time', required=True, help_text="Время выполнения",
                            widget=forms.TextInput(attrs={'placeholder': 'Время выполнения'}))
    price = forms.IntegerField(label='price', required=True, help_text="Цена",
                            widget=forms.TextInput(attrs={'placeholder': 'Цена'}))
    cond = forms.CharField(label='cond', help_text="Условия",
                            widget=forms.TextInput(attrs={'placeholder': 'Условия'}))
    #image


