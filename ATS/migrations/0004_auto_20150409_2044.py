# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATS', '0003_keyword_word_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='word_type',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
    ]
