# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 07:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0009_auto_20171130_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='cart',
        ),
    ]
