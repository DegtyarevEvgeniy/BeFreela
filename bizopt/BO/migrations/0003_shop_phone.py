# Generated by Django 4.0.4 on 2022-08-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0002_shop_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='phone',
            field=models.IntegerField(default='1151151515', max_length=20),
        ),
    ]
