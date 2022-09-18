# Generated by Django 4.0.4 on 2022-09-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0005_rename_removeimg_product_buy_previmg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_partner',
            name='id_creator',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comments_partner',
            name='id_partner',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comments_partner',
            name='review',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comments_product',
            name='comentator_email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comments_product',
            name='id_creator',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comments_product',
            name='id_product',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comments_product',
            name='review',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='last_login',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name_full',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name_small',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='payment_account',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='partner',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='compound',
            field=models.CharField(default='', max_length=50, verbose_name='Срок получения товара'),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='delivery_address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='duration',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='id_creator',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='id_user_buy',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='message',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='price',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='product_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='size',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='product_buy',
            name='status',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='availability',
            field=models.CharField(default='', max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='brand',
            field=models.CharField(default='', max_length=30, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='category',
            field=models.CharField(default='', max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='compound',
            field=models.CharField(default='', max_length=50, verbose_name='Срок получения товара'),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='country',
            field=models.CharField(default='', max_length=30, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='description',
            field=models.CharField(default='', max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='duration',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='id_creator',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='product_name',
            field=models.CharField(default='', max_length=500, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='sex',
            field=models.CharField(default='', max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product_creator',
            name='size',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='shop',
            name='category',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='id_creator',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='id_user_do',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status1',
            field=models.CharField(default='', max_length=20),
        ),
    ]