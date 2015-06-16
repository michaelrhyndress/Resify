# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessgroup',
            name='lat',
            field=models.FloatField(null=True, verbose_name=b'Latitude', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businessgroup',
            name='lon',
            field=models.FloatField(null=True, verbose_name=b'Longitude', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='businessgroup',
            name='country',
            field=models.CharField(default=b'USA', max_length=100, verbose_name=b'Country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='businessgroup',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 25, 21, 27, 50, 631293, tzinfo=utc), verbose_name=b'Date created', auto_now_add=True),
            preserve_default=True,
        ),
    ]
