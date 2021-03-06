# Generated by Django 4.0.4 on 2022-04-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_account_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='inn',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='nameFull',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='account',
            name='name_small',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='account',
            name='payment_account',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='reg_form',
            field=models.CharField(default='', max_length=20),
        ),
    ]
