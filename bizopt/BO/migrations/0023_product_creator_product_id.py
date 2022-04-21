# Generated by Django 4.0.4 on 2022-04-21 16:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0022_rename_parter_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_creator',
            name='product_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
