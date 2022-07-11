from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers


class MyAccountManager(BaseUserManager):
    def create_user(self, phone, username, password, email=None, first_name=None, last_name=None, city=''):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            city=city
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password, first_name, last_name, city=''):
        user = self.create_user(
            phone=phone,
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            city=city
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=20, default='', unique=True)
    email = models.EmailField(default='', unique=True)
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=30, default='')
    phone = models.IntegerField(unique=True)
    city = models.CharField(max_length=30, default='')
    userImage = models.ImageField(upload_to='images/', default='images/default.png')
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    inn = models.IntegerField(default=0)
    name_small = models.CharField(max_length=20,default='')
    nameFull = models.CharField(max_length=20,default='')
    payment_account = models.IntegerField(default=0)
    reg_form = models.CharField(max_length=20,default='')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return str(self.phone)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
