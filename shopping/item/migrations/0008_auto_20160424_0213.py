# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import item.models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_itemreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image1',
            field=models.ImageField(blank=True, upload_to=item.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='item',
            name='image2',
            field=models.ImageField(blank=True, upload_to=item.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='item',
            name='image3',
            field=models.ImageField(blank=True, upload_to=item.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='item',
            name='image4',
            field=models.ImageField(blank=True, upload_to=item.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='item',
            name='image5',
            field=models.ImageField(blank=True, upload_to=item.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='item',
            name='image6',
            field=models.ImageField(blank=True, upload_to=item.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='item',
            name='image7',
            field=models.ImageField(blank=True, upload_to=item.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='item',
            name='image8',
            field=models.ImageField(blank=True, upload_to=item.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='item',
            name='image9',
            field=models.ImageField(blank=True, upload_to=item.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='itemqna',
            name='answer',
            field=models.TextField(blank=True, default='답변 전 입니다.'),
        ),
    ]
