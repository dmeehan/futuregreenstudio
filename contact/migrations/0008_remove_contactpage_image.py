# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-05-22 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20230522_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='image',
        ),
    ]
