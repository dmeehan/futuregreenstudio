# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170920_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagegalleryitem',
            name='theme',
            field=models.CharField(choices=[('dark', 'Dark'), ('light', 'Light')], default='dark', max_length=255),
        ),
    ]
