# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampling_event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='accountable',
            field=models.BooleanField(default=True),
        ),
    ]
