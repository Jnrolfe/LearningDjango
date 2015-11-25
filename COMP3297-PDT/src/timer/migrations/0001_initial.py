# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0005_iteration_developer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('start_time', models.PositiveIntegerField(default=0)),
                ('end_time', models.PositiveIntegerField(default=0)),
                ('elapsed_time', models.PositiveIntegerField(default=0)),
                ('running_total', models.PositiveIntegerField(default=0)),
                ('iteration', models.ForeignKey(blank=True, to='project.Iteration', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
