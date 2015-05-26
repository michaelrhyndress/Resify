# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0002_auto_20150525_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessgroup',
            name='city',
            field=models.CharField(max_length=100, verbose_name=b'City'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='businessgroup',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 25, 22, 6, 59, 416345, tzinfo=utc), verbose_name=b'Date created', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='businessgroup',
            name='street_line1',
            field=models.CharField(max_length=100, verbose_name=b'Address 1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='businessgroup',
            name='zipcode',
            field=models.CharField(max_length=5, verbose_name=b'ZIP code'),
            preserve_default=True,
        ),
    ]
