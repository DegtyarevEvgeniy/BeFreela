# Generated by Django 4.0 on 2022-03-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0004_rename_avatar_user_userimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='-', max_length=500)),
                ('cost', models.IntegerField(default=0)),
                ('availability', models.CharField(default='-', max_length=100)),
                ('description', models.CharField(default='-', max_length=1000)),
            ],
        ),
    ]
