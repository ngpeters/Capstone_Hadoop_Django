# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockcatalog', '0002_auto_20180410_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stockgraph',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
