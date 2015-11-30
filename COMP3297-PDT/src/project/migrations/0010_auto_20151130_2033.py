# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20151127_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defectdata',
            name='total_defects',
        ),
        migrations.AddField(
            model_name='defectdata',
            name='defect_type',
            field=models.CharField(default='type 1 defect', max_length=30),
        ),
    ]
