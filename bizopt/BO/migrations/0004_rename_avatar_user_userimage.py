# Generated by Django 4.0 on 2022-03-05 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0003_creator_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avatar',
            new_name='userImage',
        ),
    ]