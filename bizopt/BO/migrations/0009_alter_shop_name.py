# Generated by Django 4.0.4 on 2022-08-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0008_alter_shop_email_alter_shop_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
