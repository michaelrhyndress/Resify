# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_auto_20150413_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 23, 3, 17, 188213, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 20, 23, 3, 17, 188596, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_skills',
            name='skill',
            field=models.ForeignKey(to='Registration.Skills', null=True),
            preserve_default=True,
        ),
    ]
