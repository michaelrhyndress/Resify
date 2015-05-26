# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admin', models.EmailField(max_length=255, verbose_name=b'Owner')),
                ('name', models.CharField(max_length=255, verbose_name=b'Business name')),
                ('corporation', models.CharField(max_length=100, verbose_name=b'Corporation', blank=True)),
                ('departement', models.CharField(max_length=50, verbose_name=b'Departement', blank=True)),
                ('phone_number', models.CharField(max_length=30, verbose_name=b'Phone number', blank=True)),
                ('description', models.TextField(default=b'Description Not Available', verbose_name=b'Description')),
                ('website', models.URLField(verbose_name=b'Website', blank=True)),
                ('building', models.CharField(max_length=20, verbose_name=b'Building', blank=True)),
                ('floor', models.CharField(max_length=20, verbose_name=b'Floor', blank=True)),
                ('door', models.CharField(max_length=20, verbose_name=b'Door', blank=True)),
                ('number', models.CharField(max_length=30, verbose_name=b'Number', blank=True)),
                ('street_line1', models.CharField(max_length=100, verbose_name=b'Address 1', blank=True)),
                ('street_line2', models.CharField(max_length=100, verbose_name=b'Address 2', blank=True)),
                ('city', models.CharField(max_length=100, verbose_name=b'City', blank=True)),
                ('state', localflavor.us.models.USStateField(max_length=2, verbose_name=b'State', choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AS', b'American Samoa'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'AA', b'Armed Forces Americas'), (b'AE', b'Armed Forces Europe'), (b'AP', b'Armed Forces Pacific'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'GU', b'Guam'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'MP', b'Northern Mariana Islands'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'PR', b'Puerto Rico'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VI', b'Virgin Islands'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
                ('country', models.CharField(default=b'United States', max_length=100, verbose_name=b'Country')),
                ('postal_box', models.CharField(max_length=20, verbose_name=b'Postal box', blank=True)),
                ('zipcode', models.CharField(max_length=5, verbose_name=b'ZIP code', blank=True)),
                ('created_date', models.DateField(default=datetime.datetime(2015, 5, 25, 20, 40, 15, 864645, tzinfo=utc), verbose_name=b'Date created', auto_now_add=True)),
                ('deleted_date', models.DateField(verbose_name=b'Date deleted', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is active')),
                ('is_locked', models.BooleanField(default=False, verbose_name=b'Is locked')),
                ('banned', models.ManyToManyField(related_name='Banned', to=settings.AUTH_USER_MODEL, blank=True)),
                ('members', models.ManyToManyField(related_name='Members', to=settings.AUTH_USER_MODEL, blank=True)),
                ('subscribed', models.ManyToManyField(related_name='Subscribed', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
