# Generated by Django 4.0.6 on 2022-08-31 14:30

import datetime
from django.db import migrations, models
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100000)),
                ('user1', models.IntegerField()),
                ('user2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments_partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_creator', models.CharField(default='-', max_length=200)),
                ('id_partner', models.CharField(default='-', max_length=200)),
                ('review', models.CharField(default='-', max_length=200)),
                ('rating', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Comments_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_creator', models.CharField(default='-', max_length=200)),
                ('comentator_email', models.CharField(default='-', max_length=200)),
                ('id_product', models.CharField(default='-', max_length=200)),
                ('review', models.CharField(default='-', max_length=200)),
                ('rating', models.IntegerField(default='0')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=1000000)),
                ('room', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='', max_length=50)),
                ('last_login', models.CharField(default='-', max_length=200)),
                ('username', models.CharField(default='-', max_length=200)),
                ('email', models.CharField(default='-', max_length=200)),
                ('first_name', models.CharField(default='-', max_length=200)),
                ('last_name', models.CharField(default='-', max_length=200)),
                ('country', models.CharField(default='-', max_length=200)),
                ('inn', models.IntegerField(default='0000000000')),
                ('name_small', models.CharField(default='-', max_length=200)),
                ('name_full', models.CharField(default='-', max_length=200)),
                ('reg_form', models.CharField(default='Самозанятый', max_length=200)),
                ('payment_account', models.CharField(default='-', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product_buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_creator', models.CharField(default='-', max_length=200)),
                ('id_user_buy', models.CharField(default='-', max_length=200)),
                ('price', models.CharField(default='-', max_length=200)),
                ('duration', models.CharField(default='-', max_length=200)),
                ('compound', models.CharField(default='-', max_length=50, verbose_name='Срок получения товара')),
                ('size', models.CharField(default='-', max_length=300)),
                ('product_name', models.CharField(default='-', max_length=500)),
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(default='-', max_length=200)),
                ('message', models.CharField(default='-', max_length=200)),
                ('payed_partner', models.BooleanField(default=0)),
                ('payed_user', models.BooleanField(default=0)),
                ('status_pay', models.BooleanField(default=0)),
                ('delivery_address', models.CharField(default='-', max_length=500)),
                ('date_add', models.DateField(default='2000-01-01', max_length=50)),
                ('img', models.ImageField(default='images/default.webp', upload_to='images/products')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('logoImage', models.ImageField(default='images/default.png', upload_to='images/creator/logoImage')),
                ('bgImage', models.ImageField(default='images/default.png', upload_to='images/creator/bgImage')),
                ('description', models.CharField(default='-', max_length=500)),
                ('category', models.CharField(default='-', max_length=500)),
                ('status', models.CharField(default='', max_length=500)),
                ('email', models.CharField(default='example@example.com', max_length=60)),
                ('phone', models.CharField(default='+15-15-15-15', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_creator', models.CharField(default='-', max_length=200)),
                ('status1', models.CharField(default='-', max_length=20)),
                ('id_user_do', models.CharField(default='-', max_length=20)),
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(default='anonymous', max_length=50)),
                ('select', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='-', max_length=500)),
                ('price', models.IntegerField(default='')),
                ('time', models.DateField(default='2000-01-01', max_length=50)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Product_creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id_creator', models.CharField(default='-', max_length=200)),
                ('product_name', models.CharField(default='-', max_length=500, verbose_name='Название')),
                ('country', models.CharField(default='-', max_length=30, verbose_name='Страна')),
                ('brand', models.CharField(default='-', max_length=30, verbose_name='Бренд')),
                ('rate_sum', models.IntegerField(default=0)),
                ('vote_sum', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('category', models.CharField(default='-', max_length=50, verbose_name='Категория')),
                ('sex', models.CharField(default='-', max_length=50, verbose_name='Категория')),
                ('compound', models.CharField(default='-', max_length=50, verbose_name='Срок получения товара')),
                ('size', models.CharField(default='-', max_length=300)),
                ('duration', models.CharField(default='-', max_length=300)),
                ('price', models.CharField(default=0, max_length=300)),
                ('show_price', models.CharField(default=0, max_length=300)),
                ('description', models.CharField(default='-', max_length=1000, verbose_name='Описание')),
                ('availability', models.CharField(default='-', max_length=100, verbose_name='')),
                ('picture', models.ImageField(default='images/default.webp', upload_to='images/product', verbose_name='')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
