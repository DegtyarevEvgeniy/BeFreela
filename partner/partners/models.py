from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers


class MyAccountManager(BaseUserManager):
    def create_user(self, email,  password=None, first_name=None, last_name=None,  city=''):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            city=city
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name, city=''):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            city=city
        )
        user.is_admin = True 
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Partner(AbstractBaseUser):
    email = models.EmailField(default='', unique=True)
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    userImage = models.ImageField(upload_to='images/', default='images/default.png')
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    inn = models.IntegerField(default=0)
    name_small = models.CharField(max_length=20, default='')
    nameFull = models.CharField(max_length=20, default='')
    payment_account = models.IntegerField(default=0)
    reg_form = models.CharField(max_length=20,default='')
    ogrn = models.IntegerField(default=0)
    korr_check = models.IntegerField(default=0)
    kpp = models.IntegerField(default=0)
    index = models.IntegerField(default=0)
    bik = models.IntegerField(default=0)
    checking_account = models.IntegerField(default=0)
    fiz_adress = models.CharField(max_length=200, default='')
    street = models.CharField(max_length=200, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True