# Generated by Django 4.0.4 on 2022-09-06 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0004_alter_product_buy_removeimg_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_buy',
            old_name='removeImg',
            new_name='prevImg',
        ),
        migrations.RenameField(
            model_name='product_creator',
            old_name='removePicture',
            new_name='prevPicture',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='removeBgImage',
            new_name='prevBgImage',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='removeLogoImage',
            new_name='prevLogoImage',
        ),
    ]
