# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 22:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missionName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='plate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sporeCount24', models.CharField(max_length=10)),
                ('sporeCount48', models.CharField(max_length=10)),
                ('sporeCount72', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PooledID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('accountable', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=400)),
                ('PooledID', smart_selects.db_fields.ChainedForeignKey(chained_field='Zone', chained_model_field='Zone', on_delete=django.db.models.deletion.CASCADE, to='sampling_event.PooledID')),
            ],
        ),
        migrations.CreateModel(
            name='sampleEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('assayName', models.CharField(max_length=100)),
                ('coge', models.CharField(max_length=100)),
                ('facility', models.CharField(max_length=100)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampling_event.Environment')),
                ('mission', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sampling_event.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='Sampler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('mission', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sampling_event.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='SampleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=10)),
                ('efficiency', models.IntegerField()),
                ('area', models.IntegerField()),
                ('volume', models.DecimalField(decimal_places=4, max_digits=10)),
                ('platesCreated', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Spacecraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mission', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sampling_event.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mission', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sampling_event.Mission')),
            ],
        ),
        migrations.AddField(
            model_name='sampleevent',
            name='samplers',
            field=models.ManyToManyField(to='sampling_event.Sampler'),
        ),
        migrations.AddField(
            model_name='sampleevent',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sampling_event.Site'),
        ),
        migrations.AddField(
            model_name='sample',
            name='Zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampling_event.Zone'),
        ),
        migrations.AddField(
            model_name='sample',
            name='sampleType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampling_event.SampleType'),
        ),
        migrations.AddField(
            model_name='sample',
            name='samplingEvent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampling_event.sampleEvent'),
        ),
        migrations.AddField(
            model_name='pooledid',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampling_event.Zone'),
        ),
        migrations.AddField(
            model_name='plate',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampling_event.sample'),
        ),
    ]
