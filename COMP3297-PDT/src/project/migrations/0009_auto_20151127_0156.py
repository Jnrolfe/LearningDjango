# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20151127_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportsloc',
            name='developer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
