# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_remove_buy_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='productInfo',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
