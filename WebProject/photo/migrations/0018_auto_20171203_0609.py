# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0017_order_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_list',
            old_name='email1',
            new_name='mail1',
        ),
    ]