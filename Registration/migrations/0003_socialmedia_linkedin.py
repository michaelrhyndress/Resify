# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_auto_20141014_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='linkedIn',
            field=models.URLField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
