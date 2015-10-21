# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='EatingInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('meal_time', models.CharField(max_length=255, choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('activity_date', models.DateField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('profile', modelcluster.fields.ParentalKey(to='health_records.HealthProfile', related_name='records')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhysActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('activity_type', models.CharField(max_length=255, choices=[('pushups', 'Pushups'), ('situps', 'Situps'), ('crunches', 'Crunches'), ('pullups', 'Pullups'), ('bench_presses', 'Bench Presses'), ('jogging', 'Jogging'), ('walking', 'Walking'), ('biking', 'Biking')])),
                ('duration', models.IntegerField(help_text='The duration of the activity in minutes.')),
                ('reps', models.IntegerField(help_text='Number of times you performed the exercise.')),
                ('record', modelcluster.fields.ParentalKey(to='health_records.HealthRecord', related_name='physical_activity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='eatinginfo',
            name='record',
            field=modelcluster.fields.ParentalKey(to='health_records.HealthRecord', related_name='eating_info'),
        ),
    ]
