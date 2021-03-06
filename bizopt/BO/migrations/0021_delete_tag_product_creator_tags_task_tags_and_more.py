# Generated by Django 4.0 on 2022-04-16 16:27

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('BO', '0020_product_buy_product_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='product_creator',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateField(default='-', max_length=50),
        ),
    ]
