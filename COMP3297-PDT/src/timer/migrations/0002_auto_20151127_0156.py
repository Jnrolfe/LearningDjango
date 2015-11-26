# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='elapsed_time',
            field=models.DecimalField(decimal_places=1, max_digits=7, default=0.0),
        ),
        migrations.AlterField(
            model_name='timer',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='timer',
            name='running_total',
            field=models.DecimalField(decimal_places=1, max_digits=7, default=0.0),
        ),
        migrations.AlterField(
            model_name='timer',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
