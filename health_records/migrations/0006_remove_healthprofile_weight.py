# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_records', '0005_healthprofile_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthprofile',
            name='weight',
        ),
    ]
