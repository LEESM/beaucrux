# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 08:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20160511_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
