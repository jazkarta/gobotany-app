# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxon',
            options={'ordering': ['scientific_name'], 'verbose_name': 'taxon', 'verbose_name_plural': 'taxa', 'permissions': (('botanist', 'botanist'),)},
        ),
        migrations.AlterField(
            model_name='conservationstatus',
            name='region',
            field=models.CharField(max_length=80, choices=[(b'AL', 'Alabama'), (b'AK', 'Alaska'), (b'AB', 'Alberta'), (b'AZ', 'Arizona'), (b'AR', 'Arkansas'), (b'BC', 'British Columbia'), (b'CA', 'California'), (b'CO', 'Colorado'), (b'CT', 'Connecticut'), (b'DE', 'Delaware'), (b'DC', 'District of Columbia'), (b'FL', 'Florida'), (b'GA', 'Georgia'), (b'HI', 'Hawaii'), (b'ID', 'Idaho'), (b'IL', 'Illinois'), (b'IN', 'Indiana'), (b'IA', 'Iowa'), (b'KS', 'Kansas'), (b'KY', 'Kentucky'), (b'LA', 'Louisiana'), (b'ME', 'Maine'), (b'MB', 'Manitoba'), (b'MD', 'Maryland'), (b'MA', 'Massachusetts'), (b'MI', 'Michigan'), (b'MN', 'Minnesota'), (b'MS', 'Mississippi'), (b'MO', 'Missouri'), (b'MT', 'Montana'), (b'NE', 'Nebraska'), (b'NV', 'Nevada'), (b'NB', 'New Brunswick'), (b'NH', 'New Hampshire'), (b'NJ', 'New Jersey'), (b'NM', 'New Mexico'), (b'NY', 'New York'), (b'NL', 'Newfoundland and Labrador'), (b'NC', 'North Carolina'), (b'ND', 'North Dakota'), (b'NT', 'Northwest Territories'), (b'NS', 'Nova Scotia'), (b'NU', 'Nunavut'), (b'OH', 'Ohio'), (b'OK', 'Oklahoma'), (b'ON', 'Ontario'), (b'OR', 'Oregon'), (b'PA', 'Pennsylvania'), (b'PE', 'Prince Edward Island'), (b'QC', 'Quebec'), (b'RI', 'Rhode Island'), (b'SK', 'Saskatchewan'), (b'SC', 'South Carolina'), (b'SD', 'South Dakota'), (b'TN', 'Tennessee'), (b'TX', 'Texas'), (b'UT', 'Utah'), (b'VT', 'Vermont'), (b'VA', 'Virginia'), (b'WA', 'Washington'), (b'WV', 'West Virginia'), (b'WI', 'Wisconsin'), (b'WY', 'Wyoming'), (b'YT', 'Yukon')]),
        ),
        migrations.AlterField(
            model_name='copyrightholder',
            name='contact_info',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='copyrightholder',
            name='date_record',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='copyrightholder',
            name='notes',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='copyrightholder',
            name='permission_level',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='copyrightholder',
            name='permission_location',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='copyrightholder',
            name='permission_source',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='copyrightholder',
            name='primary_bds',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='copyrightholder',
            name='source',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='invasivestatus',
            name='region',
            field=models.CharField(max_length=80, choices=[(b'ab', 'Alberta'), (b'ak', 'Alaska'), (b'al', 'Alabama'), (b'ar', 'Arkansas'), (b'az', 'Arizona'), (b'bc', 'British Columbia'), (b'ca', 'California'), (b'co', 'Colorado'), (b'ct', 'Connecticut'), (b'dc', 'District of Columbia'), (b'de', 'Delaware'), (b'fl', 'Florida'), (b'ga', 'Georgia'), (b'hi', 'Hawaii'), (b'ia', 'Iowa'), (b'id', 'Idaho'), (b'il', 'Illinois'), (b'in', 'Indiana'), (b'ks', 'Kansas'), (b'ky', 'Kentucky'), (b'la', 'Louisiana'), (b'ma', 'Massachusetts'), (b'mb', 'Manitoba'), (b'md', 'Maryland'), (b'me', 'Maine'), (b'mi', 'Michigan'), (b'mn', 'Minnesota'), (b'mo', 'Missouri'), (b'ms', 'Mississippi'), (b'mt', 'Montana'), (b'nb', 'New Brunswick'), (b'nc', 'North Carolina'), (b'nd', 'North Dakota'), (b'ne', 'Nebraska'), (b'nh', 'New Hampshire'), (b'nj', 'New Jersey'), (b'nl', 'Newfoundland and Labrador'), (b'nm', 'New Mexico'), (b'ns', 'Nova Scotia'), (b'nt', 'Northwest Territories'), (b'nu', 'Nunavut'), (b'nv', 'Nevada'), (b'ny', 'New York'), (b'oh', 'Ohio'), (b'ok', 'Oklahoma'), (b'on', 'Ontario'), (b'or', 'Oregon'), (b'pa', 'Pennsylvania'), (b'pe', 'Prince Edward Island'), (b'qc', 'Quebec'), (b'ri', 'Rhode Island'), (b'sc', 'South Carolina'), (b'sd', 'South Dakota'), (b'sk', 'Saskatchewan'), (b'tn', 'Tennessee'), (b'tx', 'Texas'), (b'ut', 'Utah'), (b'va', 'Virginia'), (b'vt', 'Vermont'), (b'wa', 'Washington'), (b'wi', 'Wisconsin'), (b'wv', 'West Virginia'), (b'wy', 'Wyoming'), (b'yt', 'Yukon')]),
        ),
    ]
