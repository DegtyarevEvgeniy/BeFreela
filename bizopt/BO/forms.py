from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Логин', required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль', required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))
    # phone = forms.IntegerField(label='Телефон', widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    name = forms.CharField(label='Имя', max_length=20,
                           widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(label='Фамилия', max_length=30,
                              widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    # city = forms.CharField(label='Город', max_length=20,
    #                        widget=forms.TextInput(attrs={'placeholder': 'Город'}))
    # email = forms.CharField(label='Почта', max_length=20,
    #                         widget=forms.TextInput(attrs={'placeholder': 'Почта'}))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class ProductCreationForm(forms.Form):
    product_name = forms.CharField(required=True)
    cost = forms.CharField(required=True)
    availability = forms.ChoiceField()
    description = forms.CharField()
    picture = forms.ImageField()


class addTasks(forms.Form):
    data = (
        (1, "v1"),
        (2, "v2"),
        (3, "v3"),
    )
    task_name = forms.CharField(label='Название', required=True, widget=forms.TextInput(attrs={'placeholder': 'Название'}))
    select = forms.ChoiceField(label='Теги', choices=data, widget=forms.Select)
    description = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'placeholder': 'Описание'}))
    price = forms.IntegerField(label='Цена', required=True, widget=forms.TextInput(attrs={'placeholder': 'Цена'}))
    data = forms.DateField(label='Дата', widget=forms.TextInput(attrs={'placeholder': 'Дата'}))
