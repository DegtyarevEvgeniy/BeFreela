from django.db import models

# Create your models here.
class Pers(models.Model):
    name = models.CharField(max_length=20, default='__', unique=True)
    desc = models.CharField(max_length=200, default='__')
    age = models.IntegerField(default=0)