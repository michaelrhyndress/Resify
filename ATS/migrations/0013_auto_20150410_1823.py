# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATS', '0012_auto_20150410_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='words',
            field=models.ManyToManyField(to='ATS.Keyword', blank=True),
            preserve_default=True,
        ),
    ]
