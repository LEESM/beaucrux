# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-24 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0016_item_is_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='order_number',
            field=models.IntegerField(default=0),
        ),
    ]