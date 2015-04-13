# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_auto_20150412_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 19, 11, 35, 795252, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 13, 19, 11, 35, 795539, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='handle',
            field=models.SlugField(default=b'', unique=True, max_length=25, blank=True),
            preserve_default=True,
        ),
    ]
