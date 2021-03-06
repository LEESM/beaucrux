# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-18 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import item.models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0018_brand_brand_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_to_subject', models.CharField(max_length=100)),
                ('content_to_url', models.CharField(max_length=100)),
                ('content_to_img', models.ImageField(blank=True, upload_to=item.models.get_image_path)),
                ('item_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item1', to='item.Item')),
                ('item_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item2', to='item.Item')),
            ],
        ),
    ]
