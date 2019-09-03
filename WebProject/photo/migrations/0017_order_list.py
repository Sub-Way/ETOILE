# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0016_auto_20171203_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now=True, verbose_name='order_date')),
                ('name1', models.CharField(max_length=100)),
                ('email1', models.CharField(max_length=100)),
                ('phone1', models.CharField(default='010', max_length=3)),
                ('phone2', models.CharField(default='2050', max_length=4)),
                ('phone3', models.CharField(default='8194', max_length=4)),
                ('name2', models.CharField(max_length=100)),
                ('phone4', models.CharField(default='010', max_length=3)),
                ('phone5', models.CharField(default='3524', max_length=4)),
                ('phone6', models.CharField(default='6342', max_length=4)),
                ('add1', models.CharField(max_length=100)),
                ('add2', models.CharField(max_length=100)),
                ('add3', models.CharField(max_length=100)),
                ('memo', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Album')),
            ],
        ),
    ]