# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-10 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crn', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('hour', models.IntegerField()),
                ('intersect_type', models.CharField(max_length=30)),
                ('collision_type', models.CharField(max_length=30)),
                ('fatal_count', models.IntegerField()),
                ('injury_count', models.IntegerField()),
                ('sev_inj_count', models.IntegerField()),
                ('maj_inj_count', models.IntegerField()),
                ('mcycle_death_count', models.IntegerField()),
                ('mcycle_sev_inj_count', models.IntegerField()),
                ('bicycle_death_count', models.IntegerField()),
                ('bicycle_sev_inj_count', models.IntegerField()),
                ('ped_death_count', models.IntegerField()),
                ('max_severity_level', models.CharField(max_length=30)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='crashFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='crash/')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crn', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('person_type', models.CharField(max_length=30)),
                ('restraint_helmet', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='personFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='person/')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crn', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='vehicleFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='vehicle/')),
            ],
        ),
    ]
