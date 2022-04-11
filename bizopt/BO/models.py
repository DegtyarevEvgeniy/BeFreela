import uuid
from django.db import models
from django.forms import ModelForm

class Creator(models.Model):
    first_name = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=20, default='example@example.com')
    cover = models.ImageField(upload_to='images/creator', default='images/default.png')
    description = models.CharField(max_length=500, default='-')
    is_company = models.BooleanField(default=0)
    company_name = models.CharField(max_length=50, default='-')
    telegram = models.CharField(max_length=50, default='-')
    vk = models.CharField(max_length=50, default='-')
    whatsapp = models.CharField(max_length=50, default='-')
    instagram = models.CharField(max_length=50, default='-')
    tag = models.CharField(max_length=50, default='-')
    published = models.BooleanField(default=1)


class Product_buy(models.Model):
    id_creator = models.CharField(max_length=200, default='-') #кто создал
    id_user_buy = models.CharField(max_length=200, default='-') #кто покупает
    task_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status1 = models.CharField(max_length=20, default='-') #запрос в работе
    status2 = models.CharField(max_length=20, default='-') #в ожидании в работе готово


class Product_creator(models.Model):
    id_creator = models.CharField(max_length=200, default='-') #кто создал
    product_name = models.CharField('Название', max_length=500, default='-')
    country = models.CharField('Страна', max_length=30, default='-')
    brand = models.CharField('Бренд', max_length=30, default='-')
    # set = list
    price = models.IntegerField('Цена', default=0)
    description = models.CharField('Описание', max_length=1000, default='-')
    # keywords = list
    width_product = models.FloatField('', default=0)
    height_product = models.FloatField('', default=0)
    length_product = models.FloatField('', default=0)
    width_packaging = models.FloatField('', default=0)
    height_packaging = models.FloatField('', default=0)
    length_packaging = models.FloatField('', default=0)
    availability = models.CharField('', max_length=100, default='-')
    picture = models.ImageField('', upload_to='images/product',
                                default='images/default.png')


class Task(models.Model):
    id_creator = models.CharField(max_length=200, default='-') #кто создал
    status1 = models.CharField(max_length=20, default='-')
    id_user_do = models.CharField(max_length=20, default='-') #кто делает
    task_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, default='anonymous')
    select = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='-')
    price = models.IntegerField(default='')
    time = models.CharField(max_length=50, default='-')


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, default='')


class Hashtags(models.Model):
    tag_name = models.CharField(max_length=50, default='')
