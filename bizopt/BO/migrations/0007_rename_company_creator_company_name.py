# Generated by Django 4.0 on 2022-03-18 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0006_creator_activity_type_creator_is_company_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creator',
            old_name='company',
            new_name='company_name',
        ),
    ]