# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-29 20:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_auto_20180730_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='sender'),
        ),
    ]
