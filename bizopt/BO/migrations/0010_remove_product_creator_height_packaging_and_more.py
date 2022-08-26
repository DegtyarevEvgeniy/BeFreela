# Generated by Django 4.0.6 on 2022-08-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0009_alter_product_creator_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_creator',
            name='height_packaging',
        ),
        migrations.RemoveField(
            model_name='product_creator',
            name='height_product',
        ),
        migrations.RemoveField(
            model_name='product_creator',
            name='length_packaging',
        ),
        migrations.RemoveField(
            model_name='product_creator',
            name='length_product',
        ),
        migrations.RemoveField(
            model_name='product_creator',
            name='width_packaging',
        ),
        migrations.RemoveField(
            model_name='product_creator',
            name='width_product',
        ),
        migrations.AddField(
            model_name='product_buy',
            name='compound',
            field=models.CharField(default='-', max_length=50, verbose_name='Срок получения товара'),
        ),
        migrations.AddField(
            model_name='product_buy',
            name='size',
            field=models.CharField(default='-', max_length=300),
        ),
    ]