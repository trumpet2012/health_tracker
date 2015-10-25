# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def load_initial_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    HealthProfile = apps.get_model('health_records', 'HealthProfile')

    spidey, created = User.objects.get_or_create(username='spidey', first_name='Peter', last_name='Parker')
    spidey_health = HealthProfile.objects.get_or_create(user=spidey)

    tholliday, created = User.objects.get_or_create(username='trent', defaults={
        'first_name': 'Trent',
        'last_name': 'Holliday',
    })
    tholliday.first_name = 'Trent'
    tholliday.last_name = 'Holliday'
    tholliday.save()
    tholliday_health = HealthProfile.objects.get_or_create(user=tholliday)

    bruce, created = User.objects.get_or_create(username='bats', first_name='Bruce', last_name='Wayne')
    bruce_health = HealthProfile.objects.get_or_create(user=bruce)

    alfred, created = User.objects.get_or_create(username='alfred', first_name='Alfred', last_name='Pennyworth')
    alfred_health = HealthProfile.objects.get_or_create(user=alfred)


class Migration(migrations.Migration):

    dependencies = [
        ('health_records', '0002_auto_20151021_2049'),
    ]

    operations = [
        migrations.RunPython(load_initial_profiles)
    ]
