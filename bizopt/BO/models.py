from django.db import models
from django.forms import ModelForm

class User(models.Model):
    login = models.CharField(max_length=20, default='anonymous', unique=True)
    password = models.CharField(max_length=20, default='12345678')
    email = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=20, default='')
    surname = models.CharField(max_length=30, default='')
    phone = models.IntegerField(default='')
    city = models.CharField(max_length=20, default='')
    userImage = models.ImageField(upload_to='images/', default='images/default.png')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'email', 'name', 'surname', 'phone', 'city']


class Orders(models.Model):
    user = models.CharField(max_length=20, default='anonymous')
    description = models.CharField(max_length=500, default='-')
    type = models.CharField(max_length=20, default='-')
    delivery = models.CharField(max_length=20, default='-')
    price = models.IntegerField(default='')
    time = models.CharField(max_length=100, default='-')


class Creator(models.Model):
    cover = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500, default='-')
    company = models.BooleanField(default=0)
    achievements = models.ImageField(upload_to='images/')

