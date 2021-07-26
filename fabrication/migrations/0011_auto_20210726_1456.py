# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-26 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fabrication', '0010_auto_20210726_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricationmaterialpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Material Image', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
    ]
