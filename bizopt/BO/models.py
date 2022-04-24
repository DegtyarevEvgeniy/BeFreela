import uuid
from django.db import models
from django.forms import ModelForm
from taggit.managers import TaggableManager

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
    product_name = models.CharField(max_length=500, default='-')
    task_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status1 = models.CharField(max_length=20, default='-') #запрос в работе
    status2 = models.CharField(max_length=20, default='-') #в ожидании в работе готово


class Product_creator(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    id_creator = models.CharField(max_length=200, default='-') #кто создал
    product_name = models.CharField('Название', max_length=500, default='-')
    country = models.CharField('Страна', max_length=30, default='-')
    brand = models.CharField('Бренд', max_length=30, default='-')
    # set = list
    price = models.IntegerField('Цена', default=0)
    description = models.CharField('Описание', max_length=1000, default='-')
    width_product = models.FloatField('', default=0)
    height_product = models.FloatField('', default=0)
    length_product = models.FloatField('', default=0)
    width_packaging = models.FloatField('', default=0)
    height_packaging = models.FloatField('', default=0)
    length_packaging = models.FloatField('', default=0)
    availability = models.CharField('', max_length=100, default='-')
    picture = models.ImageField('', upload_to='images/product',
                                default='images/default.png')
    tags = TaggableManager()

class Task(models.Model):
    id_creator = models.CharField(max_length=200, default='-') #кто создал
    status1 = models.CharField(max_length=20, default='-')
    id_user_do = models.CharField(max_length=20, default='-') #кто делает
    task_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, default='anonymous')
    select = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='-')
    price = models.IntegerField(default='')
    time = models.DateField(max_length=50, default='-')
    tags = TaggableManager()


    def __unicode__(self):
        return self.tags


class Hashtags(models.Model):
    tag_name = models.CharField(max_length=50, default='')


class Partner(models.Model):
    password = models.CharField(max_length=50, default='')
    last_login = models.CharField(max_length=200, default='-')
    username = models.CharField(max_length=200, default='-')
    email = models.CharField(max_length=200, default='-')
    first_name = models.CharField(max_length=200, default='-')
    last_name = models.CharField(max_length=200, default='-')
    country = models.CharField(max_length=200, default='-')
    inn = models.IntegerField(default='0000000000')
    name_small = models.CharField(max_length=200, default='-')
    name_full = models.CharField(max_length=200, default='-')
    reg_form = models.CharField(max_length=200, default='-')
    payment_account = models.CharField(max_length=200, default='-')