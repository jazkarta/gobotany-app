# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150915_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcecitation',
            name='publication_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Publication Year', validators=[django.core.validators.MaxValueValidator(2016)]),
        ),
    ]
