# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0006_auto_20150520_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 23, 32, 7, 47092, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 23, 32, 7, 47481, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_skills',
            name='percentage',
            field=models.PositiveSmallIntegerField(default=0, max_length=100),
            preserve_default=True,
        ),
    ]
