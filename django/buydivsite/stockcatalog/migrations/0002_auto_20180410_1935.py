# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockcatalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfitUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a profit use (e.g. Buyback or Dividen)', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='stock',
            name='proffituse',
        ),
        migrations.DeleteModel(
            name='ProffitUse',
        ),
        migrations.AddField(
            model_name='stock',
            name='profituse',
            field=models.ManyToManyField(help_text='Select a profituse for this stock', to='stockcatalog.ProfitUse'),
        ),
    ]
