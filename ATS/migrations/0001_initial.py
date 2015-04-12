# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(unique=True, max_length=250)),
                ('popularity', models.PositiveIntegerField(default=0)),
                ('synonyms', models.ManyToManyField(related_name='synonyms_rel_+', null=True, to='ATS.Keywords', blank=True)),
            ],
            options={
                'ordering': ['word'],
            },
            bases=(models.Model,),
        ),
    ]
