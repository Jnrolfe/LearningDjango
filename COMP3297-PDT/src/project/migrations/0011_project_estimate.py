# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20151130_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='estimate',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
