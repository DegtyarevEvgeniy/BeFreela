class UserForm(forms.Form):
    login = forms.CharField(label='login', required=True)
    password = forms.CharField(label='password1', required=True)

    phone = forms.Integer(max_length=20)
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=30)
    gender = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)