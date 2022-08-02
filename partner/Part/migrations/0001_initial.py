

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('name', models.CharField(max_length=20)),

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
                ('id_product', models.CharField(default='-', max_length=200)),
                ('review', models.CharField(default='-', max_length=200)),
                ('rating', models.IntegerField(default='0')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=20, unique=True)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='example@example.com', max_length=20)),
                ('cover', models.ImageField(default='images/default.png', upload_to='images/creator')),
                ('description', models.CharField(default='-', max_length=500)),
                ('is_company', models.BooleanField(default=0)),
                ('company_name', models.CharField(default='-', max_length=50)),
                ('telegram', models.CharField(default='-', max_length=50)),
                ('vk', models.CharField(default='-', max_length=50)),
                ('whatsapp', models.CharField(default='-', max_length=50)),
                ('instagram', models.CharField(default='-', max_length=50)),
                ('tag', models.CharField(default='-', max_length=50)),
                ('published', models.BooleanField(default=1)),
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

                ('value', models.CharField(max_length=20)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=20)),
                ('room', models.CharField(max_length=20)),
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
                ('product_name', models.CharField(default='-', max_length=500)),
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(default='-', max_length=200)),
                ('message', models.CharField(default='-', max_length=200)),
                ('payed_partner', models.BooleanField(default=0)),
                ('payed_user', models.BooleanField(default=0)),
                ('status_pay', models.BooleanField(default=0)),
                ('delivery_address', models.CharField(default='-', max_length=500)),
                ('date_add', models.DateField(default='2000-01-01', max_length=50)),
                ('img', models.ImageField(default='images/default.png', upload_to='images/products')),
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
                ('rating_status', models.IntegerField(default=0)),
                ('term_status', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('set', models.CharField(default='-', max_length=300)),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('description', models.CharField(default='-', max_length=1000, verbose_name='Описание')),
                ('width_product', models.FloatField(default=0, verbose_name='')),
                ('height_product', models.FloatField(default=0, verbose_name='')),
                ('length_product', models.FloatField(default=0, verbose_name='')),
                ('width_packaging', models.FloatField(default=0, verbose_name='')),
                ('height_packaging', models.FloatField(default=0, verbose_name='')),
                ('length_packaging', models.FloatField(default=0, verbose_name='')),
                ('availability', models.CharField(default='-', max_length=100, verbose_name='')),
                ('picture', models.ImageField(default='images/default.png', upload_to='images/product', verbose_name='')),
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
            ],
        ),
    ]
