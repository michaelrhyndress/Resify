# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0004_auto_20150525_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessgroup',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 25, 22, 11, 52, 306649, tzinfo=utc), verbose_name=b'Date created', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='businessgroup',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name=b'Date deleted', blank=True),
            preserve_default=True,
        ),
    ]
