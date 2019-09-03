# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 18:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0013_album_worm'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('Csize', models.CharField(default='M', max_length=5)),
                ('line_total', models.IntegerField(default=0)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='Csize',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='album',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.Cart'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Album'),
        ),
    ]
