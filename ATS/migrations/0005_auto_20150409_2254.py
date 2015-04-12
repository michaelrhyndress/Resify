# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATS', '0004_auto_20150409_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='word_type',
            field=models.CharField(default=b'verb', max_length=15, blank=True),
            preserve_default=True,
        ),
    ]
