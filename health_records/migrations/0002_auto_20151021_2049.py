# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_records', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='healthprofile',
            options={'verbose_name': 'Health Profile'},
        ),
        migrations.AddField(
            model_name='eatinginfo',
            name='calories',
            field=models.IntegerField(default=0, help_text='The number of calories of the meal.'),
            preserve_default=False,
        ),
    ]
