# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-16 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thing',
            options={'ordering': ['-created_to']},
        ),
        migrations.RemoveField(
            model_name='thing',
            name='active',
        ),
        migrations.AddField(
            model_name='thing',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
