# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-26 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabrication', '0011_auto_20210726_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fabricationmaterialpage',
            name='name',
        ),
    ]
