# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_records', '0004_auto_20151103_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthprofile',
            name='weight',
            field=models.FloatField(default=0, help_text=b'Weight in pounds'),
            preserve_default=False,
        ),
    ]
