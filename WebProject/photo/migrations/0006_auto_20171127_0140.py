# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_auto_20171126_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='productInfo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
