# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_categories_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['name'], 'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['title'], 'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
    ]
