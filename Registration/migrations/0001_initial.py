# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=50, blank=True)),
                ('Accomplishment_from_date', models.CharField(default=b'', max_length=4, blank=True)),
                ('Accomplishment_to_date', models.CharField(default=b'', max_length=7, blank=True)),
                ('about', models.TextField(default=b'', blank=True)),
            ],
            options={
                'ordering': ['-Accomplishment_from_date'],
                'verbose_name': 'accomplishment',
                'verbose_name_plural': 'accomplishments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(default=b'', max_length=50, blank=True)),
                ('status', models.CharField(blank=True, max_length=9, choices=[(b'', b''), (b'Graduated', b'Graduated'), (b'Attending', b'Attending')])),
                ('Education_from_date', models.CharField(default=b'', max_length=4, blank=True)),
                ('Education_to_date', models.CharField(default=b'', max_length=7, blank=True)),
                ('degree', models.CharField(default=b'', max_length=100, blank=True)),
                ('about', models.TextField(default=b'', blank=True)),
            ],
            options={
                'ordering': ['-Education_from_date'],
                'verbose_name': 'education history',
                'verbose_name_plural': 'education history',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(default=b'', max_length=50, blank=True)),
                ('company', models.CharField(default=b'', max_length=50, blank=True)),
                ('job_from_date', models.CharField(default=b'', max_length=4, blank=True)),
                ('job_to_date', models.CharField(default=b'', max_length=7, blank=True)),
                ('job_about', models.TextField(default=b'', blank=True)),
            ],
            options={
                'ordering': ['-job_from_date'],
                'verbose_name': 'job history',
                'verbose_name_plural': 'job history',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=30, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook', models.URLField(default=b'', blank=True)),
                ('twitter', models.URLField(default=b'', blank=True)),
                ('gplus', models.URLField(default=b'', blank=True)),
                ('linkedIn', models.URLField(default=b'', blank=True)),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'social media',
                'verbose_name_plural': 'social media',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_name', models.CharField(default=b'Template0', unique=True, max_length=50)),
                ('readable_name', models.CharField(default=b'', max_length=50, blank=True)),
                ('is_public_template', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['template_name'],
                'verbose_name': 'template',
                'verbose_name_plural': 'templates',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percentage', models.PositiveSmallIntegerField(max_length=100, blank=True)),
                ('skill', models.ForeignKey(to='Registration.Skills')),
            ],
            options={
                'ordering': ['-percentage'],
                'verbose_name': 'user skill',
                'verbose_name_plural': 'user skills',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_name', models.ForeignKey(to='Registration.Template')),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'user template',
                'verbose_name_plural': 'user templates',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profession', models.CharField(default=b'', max_length=50, blank=True)),
                ('handle', models.SlugField(default=b'', unique=True, max_length=15, blank=True)),
                ('phone_number', models.CharField(default=b'', max_length=30, blank=True)),
                ('statement', models.TextField(default=b'', blank=True)),
                ('tags', models.ManyToManyField(to='Registration.Tag', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('first_name', models.CharField(default=b'', max_length=35, blank=True)),
                ('last_name', models.CharField(default=b'', max_length=35, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_public', models.BooleanField(default=False)),
                ('can_contact', models.BooleanField(default=True)),
                ('accept_terms', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('passed_setup', models.BooleanField(default=False)),
                ('created_date', models.DateField(default=datetime.datetime.now, auto_now_add=True)),
                ('modified_date', models.DateField(default=datetime.datetime.now, auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_template',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_skills',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job_history',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education_history',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accomplishments',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
