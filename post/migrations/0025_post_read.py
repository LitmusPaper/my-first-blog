# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-08 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
