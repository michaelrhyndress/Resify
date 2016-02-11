# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0003_auto_20150525_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessgroup',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 25, 22, 10, 40, 878181, tzinfo=utc), verbose_name=b'Date created', auto_now_add=True),
            preserve_default=True,
        ),
    ]
