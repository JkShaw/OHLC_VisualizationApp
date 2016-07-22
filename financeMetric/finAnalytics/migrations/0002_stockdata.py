# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finAnalytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_date', models.DateField(verbose_name='Date traded')),
                ('open_price', models.FloatField(default=0.0)),
                ('high_proce', models.FloatField(default=0.0)),
                ('low_price', models.FloatField(default=0.0)),
                ('close_price', models.FloatField(default=0.0)),
                ('volume', models.IntegerField(default=0)),
                ('adj_close', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
