# Generated by Django 4.1.7 on 2023-03-01 12:55

import core.staging
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CreatedAt')),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_column='UpdateAt')),
                ('title_Fr', models.CharField(blank=True, max_length=80, null=True)),
                ('description_Fr', models.TextField(blank=True, null=True)),
                ('title_En', models.CharField(blank=True, max_length=80, null=True)),
                ('description_En', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CreatedAt')),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_column='UpdateAt')),
                ('project_completed', models.IntegerField(default=0)),
                ('satisfied_client', models.IntegerField(default=0)),
                ('team_members', models.IntegerField(default=0)),
                ('bands_joined', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='CreatedAt')),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_column='UpdateAt')),
                ('title_Fr', models.CharField(blank=True, max_length=80, null=True)),
                ('description_Fr', models.TextField(blank=True, null=True)),
                ('title_En', models.CharField(blank=True, max_length=80, null=True)),
                ('description_En', models.TextField(blank=True, null=True)),
                ('header_image_url', models.ImageField(upload_to=core.staging.upload_to)),
                ('video_link_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
