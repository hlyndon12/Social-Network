# Generated by Django 3.1.4 on 2020-12-03 20:15

import django.core.validators
from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200601_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, upload_to='posts', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]