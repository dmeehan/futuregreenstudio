# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0012_auto_20171002_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='collaborator',
            options={'ordering': ['-name']},
        ),
    ]
