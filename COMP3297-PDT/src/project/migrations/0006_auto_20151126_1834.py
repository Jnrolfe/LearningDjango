# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_iteration_developer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteration',
            name='name',
            field=models.CharField(max_length=12, default='Inception', choices=[('Inception', 'inception'), ('Elaboration', 'elaboration'), ('Construction', 'construction'), ('Transition', 'transition')]),
        ),
    ]
