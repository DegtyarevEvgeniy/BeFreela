# Generated by Django 4.0.4 on 2022-08-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0002_alter_product_buy_img_alter_product_creator_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_creator',
            name='logoImage',
            field=models.ImageField(default='images/default.png', upload_to='images/creator/logoImage'),
        ),
    ]