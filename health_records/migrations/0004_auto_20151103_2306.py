# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_records', '0003_auto_20151025_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthprofile',
            name='height',
            field=models.FloatField(help_text='Height in inches', default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='healthrecord',
            name='weight',
            field=models.FloatField(help_text='Enter your weight in lbs.', default=70),
            preserve_default=False,
        ),
    ]
