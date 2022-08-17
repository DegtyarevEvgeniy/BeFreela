# sourcery skip: avoid-builtin-shadow
import uuid

from datetime import datetime

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms import ModelForm
from taggit.managers import TaggableManager
from datetime import datetime



class BoChatRoom(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    
class BoCommentsPartner(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_creator = models.CharField(max_length=200)
    id_partner = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    rating = models.IntegerField()

    


class BoCommentsProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_creator = models.CharField(max_length=200)
    id_product = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    rating = models.IntegerField()
    created_data = models.DateTimeField()

    

class BoCreator(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    cover = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_company = models.IntegerField()
    company_name = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    vk = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    published = models.IntegerField()

    


class BoHashtags(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag_name = models.CharField(max_length=50)

    

class BoMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    date = models.DateTimeField()
    user = models.TextField()
    room = models.TextField()

   


class BoPartner(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=50)
    last_login = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    inn = models.IntegerField()
    name_small = models.CharField(max_length=200)
    name_full = models.CharField(max_length=200)
    reg_form = models.CharField(max_length=200)
    payment_account = models.CharField(max_length=200)

    

class BoProductBuy(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_creator = models.CharField(max_length=200)
    id_user_buy = models.CharField(max_length=200)
    product_name = models.CharField(max_length=500)
    task_id = models.CharField(unique=True, max_length=32)
    status = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    payed_partner = models.IntegerField()
    payed_user = models.IntegerField()
    status_pay = models.IntegerField()
    delivery_address = models.CharField(max_length=500)
    date_add = models.DateField()
    img = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'BO_product_buy'


class BoProductCreator(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.CharField(unique=True, max_length=32)
    id_creator = models.CharField(max_length=200)
    product_name = models.CharField(max_length=500)
    country = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    rating_status = models.IntegerField()
    term_status = models.IntegerField()
    rating = models.FloatField()
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    set = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    width_product = models.FloatField()
    height_product = models.FloatField()
    length_product = models.FloatField()
    width_packaging = models.FloatField()
    height_packaging = models.FloatField()
    length_packaging = models.FloatField()
    availability = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)

    


class BoTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_creator = models.CharField(max_length=200)
    status1 = models.CharField(max_length=20)
    id_user_do = models.CharField(max_length=20)
    task_id = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=50)
    select = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    time = models.DateField()

   

class PartChatRoom(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    


class PartCommentsPartner(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_creator = models.CharField(max_length=200)
    id_partner = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    rating = models.IntegerField()

    

class PartCommentsProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_creator = models.CharField(max_length=200)
    id_product = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    rating = models.IntegerField()
    created_data = models.DateTimeField()

    


class PartCreator(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    cover = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_company = models.IntegerField()
    company_name = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    vk = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    published = models.IntegerField()

    


class PartHashtags(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag_name = models.CharField(max_length=50)

   


class PartMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    date = models.DateTimeField()
    user = models.TextField()
    room = models.TextField()

   

class PartProductBuy(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_creator = models.CharField(max_length=200)
    id_user_buy = models.CharField(max_length=200)
    product_name = models.CharField(max_length=500)
    task_id = models.CharField(unique=True, max_length=32)
    status = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    payed_partner = models.IntegerField()
    payed_user = models.IntegerField()
    status_pay = models.IntegerField()
    delivery_address = models.CharField(max_length=500)
    date_add = models.DateField()
    img = models.CharField(max_length=100)

   


class PartProductCreator(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.CharField(unique=True, max_length=32)
    id_creator = models.CharField(max_length=200)
    product_name = models.CharField(max_length=500)
    country = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    rating_status = models.IntegerField()
    term_status = models.IntegerField()
    rating = models.FloatField()
    set = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    width_product = models.FloatField()
    height_product = models.FloatField()
    length_product = models.FloatField()
    width_packaging = models.FloatField()
    height_packaging = models.FloatField()
    length_packaging = models.FloatField()
    availability = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)

  



class PartTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_creator = models.CharField(max_length=200)
    status1 = models.CharField(max_length=20)
    id_user_do = models.CharField(max_length=20)
    task_id = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=50)
    select = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    time = models.DateField()

    

class AccountAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=254)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    city = models.CharField(max_length=30)
    userimage = models.CharField(db_column='userImage', max_length=100)  # Field name made lowercase.
    is_admin = models.IntegerField()
    is_superuser = models.IntegerField()
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    name_small = models.CharField(max_length=20)
    namefull = models.CharField(db_column='nameFull', max_length=20)  # Field name made lowercase.
    payment_account = models.IntegerField()
    reg_form = models.CharField(max_length=20)
    inn = models.IntegerField()
    ogrn = models.IntegerField()
    korr_check = models.IntegerField()
    kpp = models.IntegerField()
    index = models.IntegerField()
    bik = models.IntegerField()
    checking_account = models.IntegerField()
    fiz_adress = models.CharField(max_length=9999)
    street = models.CharField(max_length=9999)




class PartnersPartner(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=254)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    userimage = models.CharField(db_column='userImage', max_length=100)  # Field name made lowercase.
    is_admin = models.IntegerField()
    is_superuser = models.IntegerField()
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    inn = models.IntegerField()
    name_small = models.CharField(max_length=20)
    namefull = models.CharField(db_column='nameFull', max_length=20)  # Field name made lowercase.
    payment_account = models.IntegerField()
    reg_form = models.CharField(max_length=20)
    ogrn = models.IntegerField()
    korr_check = models.IntegerField()
    kpp = models.IntegerField()
    index = models.IntegerField()
    bik = models.IntegerField()
    checking_account = models.IntegerField()
    fiz_adress = models.CharField(max_length=200)
    street = models.CharField(max_length=200)






