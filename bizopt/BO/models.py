import uuid
from django.db import models
from django.forms import ModelForm



class Orders(models.Model):
    user = models.CharField(max_length=20, default='anonymous')
    description = models.CharField(max_length=500, default='-')
    type = models.CharField(max_length=20, default='-')
    delivery = models.CharField(max_length=20, default='-')
    price = models.IntegerField(default='')
    time = models.CharField(max_length=100, default='-')


class Creator(models.Model):
    first_name = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=20, default='example@example.com')
    cover = models.ImageField(upload_to='images/creator', default='images/default.png')
    description = models.CharField(max_length=500, default='-')
    is_company = models.BooleanField(default=0)
    company_name = models.CharField(max_length=50, default='-')
    activity_type = models.CharField(max_length=70, default='-')
    achievements = models.ImageField(upload_to='images/creator')


class Product(models.Model):
    product_name = models.CharField(max_length=500, default='-')
    cost = models.IntegerField(default=0)
    availability = models.CharField(max_length=100, default='-')
    description = models.CharField(max_length=1000, default='-')
    picture = models.ImageField(upload_to='images/product',
                                default='images/default.png')


class Task(models.Model):
    task_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, default='anonymous')
    select = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='-')
    price = models.IntegerField(default='')
    time = models.DateField(default='')
