# Generated by Django 4.0.4 on 2022-09-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_account_removeuserimage_account_prevuserimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_inwaiting',
            field=models.BooleanField(default=False),
        ),
    ]
