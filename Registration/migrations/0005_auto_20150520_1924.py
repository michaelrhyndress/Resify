# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0004_auto_20150520_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 23, 24, 0, 227351, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 23, 24, 0, 227601, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_skills',
            name='skill',
            field=models.OneToOneField(null=True, to='Registration.Skills'),
            preserve_default=True,
        ),
    ]
