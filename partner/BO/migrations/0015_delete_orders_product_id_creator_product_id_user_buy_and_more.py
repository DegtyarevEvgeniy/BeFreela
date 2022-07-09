# Generated by Django 4.0.3 on 2022-04-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BO', '0014_alter_task_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.AddField(
            model_name='product',
            name='id_creator',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='id_user_buy',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='status1',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='status2',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='task',
            name='id_creator',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='id_user_do',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='task',
            name='status1',
            field=models.CharField(default='-', max_length=20),
        ),
    ]
