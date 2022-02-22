class UserForm(forms.Form):
    login = forms.CharField(label='login', required=True)
    password = forms.CharField(label='password1', required=True)

    phone = forms.IntegerField(label='login')
    name = forms.CharField(label="name", required=True)
    surname = forms.CharField(label="surname",required=True)
    city = forms.CharField(label="city")