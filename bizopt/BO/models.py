from django.db import models


class User(models.Model):
    login = models.CharField(max_length=20, default='anonymous', unique=True)
    password = models.CharField(max_length=20, default='12345678')
    sug_password = models.CharField(max_length=20, default='12345678')
    email = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=20, default='')
    surname = models.CharField(max_length=30, default='')
    phone = models.IntegerField(default='')
    city = models.CharField(max_length=20, default='')


class Orders(models.Model):
    user = models.CharField(max_length=20, default='anonymous')
    description = models.CharField(max_length=500, default='-')
    type = models.CharField(max_length=20, default='-')
    delivery = models.CharField(max_length=20, default='-')
    price = models.IntegerField(default='')
    time = models.CharField(max_length=100, default='-')



