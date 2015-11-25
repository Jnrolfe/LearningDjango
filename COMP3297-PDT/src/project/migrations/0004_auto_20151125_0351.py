# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20151125_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
