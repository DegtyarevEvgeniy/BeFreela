# Generated by Django 4.0.3 on 2022-03-22 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0008_task_creator_email_creator_first_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
