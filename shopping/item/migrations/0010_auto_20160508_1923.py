# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_auto_20160424_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemqna',
            name='secret',
            field=models.BooleanField(default=True),
        ),
    ]
