# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-09 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0084_auto_20161009_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Noter'),
        ),
    ]