import uuid
from django.db import models
from django.forms import ModelForm
from taggit.managers import TaggableManager
from datetime import datetime

class Shop(models.Model):
    name = models.CharField(max_length=50, default='')
    logoImage = models.ImageField(default='https://i.ibb.co/s3QmZrw/default.png')
    prevLogoImage = models.ImageField(default='')
    bgImage = models.ImageField(default='https://i.ibb.co/s3QmZrw/default.png')
    prevBgImage = models.ImageField(default='')
    description = models.CharField(max_length=500, default='')
    category = models.CharField(max_length=500, default='')
    status = models.CharField(max_length=500, default='')
    email = models.CharField(max_length=60, default='example@example.com')
    phone = models.CharField(max_length=20, default='')

class Product_creator(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    id_creator = models.CharField(max_length=200, default='') #кто создал
    product_name = models.CharField('Название', max_length=500, default='')
    country = models.CharField('Страна', max_length=30, default='')
    brand = models.CharField('Бренд', max_length=30, default='')
    rate_sum = models.IntegerField(default=0)
    vote_sum = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    category = models.CharField('Категория', max_length=50, default='')
    sex = models.CharField('Категория', max_length=50, default='')
    # subcategory = models.CharField('Подкатегория', max_length=50, default='')
    compound = models.CharField('Срок получения товара', max_length=50, default='')
    size = models.CharField(max_length=300, default='')
    duration = models.CharField(max_length=300, default='')
    price = models.CharField(max_length=300, default=0)
    show_price = models.CharField(max_length=300, default=0)
    description = models.CharField('Описание', max_length=1000, default='')
    availability = models.CharField('', max_length=100, default='')
    amount = models.CharField(max_length=100, default='')
    picture = models.ImageField(default='https://i.ibb.co/s3QmZrw/default.png') 
    prevPicture = models.ImageField(default='')

    tags = TaggableManager()
        # width_product = models.FloatField('', default=0)
    # height_product = models.FloatField('', default=0)
    # length_product = models.FloatField('', default=0)
    # width_packaging = models.FloatField('', default=0)
    # height_packaging = models.FloatField('', default=0)
    # length_packaging = models.FloatField('', default=0)
    # subcategory = models.CharField('Подкатегория', max_length=50, default='')

class Product_buy(models.Model):
    id_creator = models.CharField(max_length=200, default='') #кто создал
    id_user_buy = models.CharField(max_length=200, default='') #кто покупает
    price = models.CharField(max_length=200, default='')
    duration = models.CharField(max_length=200, default='')
    compound = models.CharField('Срок получения товара', max_length=50, default='')
    size = models.CharField(max_length=300, default='')
    product_name = models.CharField(max_length=500, default='')
    task_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length=200, default='')
    message = models.CharField(max_length=200, default='')
    payed_partner = models.BooleanField(default=0)
    payed_user = models.BooleanField(default=0)
    status_pay = models.BooleanField(default=0)
    delivery_address = models.CharField(max_length=500, default='')
    date_add = models.DateField(max_length=50, default='2000-01-01') 
    img = models.ImageField(default='https://i.ibb.co/s3QmZrw/default.png')
    prevImg = models.ImageField(default='')
    # status2 = models.CharField(max_length=20, default='')

class Comments_partner(models.Model):
    id_creator = models.CharField(max_length=200, default='')
    id_partner = models.CharField(max_length=200, default='')
    review = models.CharField(max_length=200, default='')
    rating = models.IntegerField(default='')


class Comments_product(models.Model):
    id_creator = models.CharField(max_length=200, default='')
    comentator_email = models.CharField(max_length=200, default='')
    id_product = models.CharField(max_length=200, default='')
    review = models.CharField(max_length=200, default='')
    rating = models.IntegerField(default='0')
    created_data = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    id_creator = models.CharField(max_length=200, default='') #кто создал
    status1 = models.CharField(max_length=20, default='')
    id_user_do = models.CharField(max_length=20, default='') #кто делает
    task_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, default='anonymous')
    select = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='')
    price = models.IntegerField(default='')
    time = models.DateField(max_length=50, default='2000-01-01')
    tags = TaggableManager()


    def __unicode__(self):
        return self.tags


class Hashtags(models.Model):
    tag_name = models.CharField(max_length=50, default='')


class Partner(models.Model):
    password = models.CharField(max_length=50, default='')
    last_login = models.CharField(max_length=200, default='')
    username = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default='')
    inn = models.IntegerField(default='0000000000')
    name_small = models.CharField(max_length=200, default='')
    name_full = models.CharField(max_length=200, default='')
    reg_form = models.CharField(max_length=200, default='Самозанятый')
    payment_account = models.CharField(max_length=200, default='')

class Chat_room(models.Model):
    name = models.CharField(max_length=100000)
    user1 = models.IntegerField()
    user2 = models.IntegerField()

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)