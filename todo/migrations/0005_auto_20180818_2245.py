# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-18 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_thing_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='text',
            field=models.TextField(max_length=1200, null=True, verbose_name='Şərh'),
        ),
    ]
