# Generated by Django 4.1.7 on 2023-02-28 23:17

import core.staging
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_header_header_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='header_image_url',
            field=models.ImageField(upload_to=core.staging.upload_to),
        ),
    ]
