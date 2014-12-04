# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education_history',
            name='status',
            field=models.CharField(blank=True, max_length=9, choices=[(b'', b''), (b'Graduated', b'Graduated'), (b'Attending', b'Attending')]),
        ),
    ]
