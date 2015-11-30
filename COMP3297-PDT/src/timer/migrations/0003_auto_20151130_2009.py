# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0002_auto_20151127_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timer',
            name='elapsed_time',
        ),
        migrations.AddField(
            model_name='timer',
            name='is_running',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='timer',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timer',
            name='running_total',
            field=models.DecimalField(max_digits=8, default=0.0, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='timer',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
