# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160424_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.AddField(
            model_name='profile',
            name='address_detail',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='profile',
            name='postcode',
            field=models.CharField(default='', max_length=10),
        ),
    ]
