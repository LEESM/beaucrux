# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='custom_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
