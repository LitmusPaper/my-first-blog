# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20180718_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=120, unique=True, verbose_name='Slug title'),
        ),
    ]
