# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-17 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20180714_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Post img'),
        ),
    ]
