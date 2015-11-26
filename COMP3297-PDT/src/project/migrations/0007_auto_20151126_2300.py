# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0006_auto_20151126_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportSLOC',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('total_lines', models.PositiveIntegerField()),
                ('developer', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='defectdata',
            name='iteration',
        ),
        migrations.RemoveField(
            model_name='defectdata',
            name='total_lines',
        ),
        migrations.AddField(
            model_name='defectdata',
            name='current_iteration',
            field=models.ForeignKey(null=True, to='project.Iteration', related_name='current_iteration', blank=True),
        ),
        migrations.AddField(
            model_name='defectdata',
            name='defect_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='defectdata',
            name='defect_iteration',
            field=models.ForeignKey(null=True, to='project.Iteration', related_name='defect_iteration', blank=True),
        ),
        migrations.AddField(
            model_name='defectdata',
            name='developer',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.RemoveField(
            model_name='iteration',
            name='developer',
        ),
        migrations.AddField(
            model_name='iteration',
            name='developer',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='iteration',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='reportsloc',
            name='iteration',
            field=models.ForeignKey(to='project.Iteration'),
        ),
    ]
