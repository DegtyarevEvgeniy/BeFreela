# Generated by Django 4.0.4 on 2022-08-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='email',
            field=models.CharField(default='example@example.com', max_length=20),
        ),
    ]
