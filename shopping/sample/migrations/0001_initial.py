# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-16 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0015_auto_20160908_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('postcode', models.CharField(max_length=32)),
                ('address1', models.CharField(max_length=128)),
                ('address2', models.CharField(max_length=128)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=128)),
                ('delivery_number', models.CharField(max_length=128)),
                ('samples', models.ManyToManyField(blank=True, to='item.Item')),
            ],
        ),
    ]
