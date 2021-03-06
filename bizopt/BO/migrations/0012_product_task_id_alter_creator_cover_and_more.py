# Generated by Django 4.0.3 on 2022-03-27 12:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0011_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='task_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='cover',
            field=models.ImageField(default='images/default.png', upload_to='images/creator'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='images/default.png', upload_to='images/product'),
        ),
    ]
