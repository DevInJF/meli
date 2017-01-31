# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('category', models.CharField(max_length=512)),
                ('photo1', models.URLField(max_length=512, null=True)),
                ('photo2', models.URLField(max_length=512, null=True)),
                ('photo3', models.URLField(max_length=512, null=True)),
                ('photo4', models.URLField(max_length=512, null=True)),
                ('photo5', models.URLField(max_length=512, null=True)),
                ('photo6', models.URLField(max_length=512, null=True)),
                ('youtube', models.CharField(max_length=512, null=True)),
                ('permalink', models.URLField(null=True)),
                ('error', models.CharField(max_length=512, null=True)),
                ('json_send', models.TextField(null=True)),
            ],
        ),
    ]
