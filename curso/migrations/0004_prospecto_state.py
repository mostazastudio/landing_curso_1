# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_prospecto_profesion'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospecto',
            name='state',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
