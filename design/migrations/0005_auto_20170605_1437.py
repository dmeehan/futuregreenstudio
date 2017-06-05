# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_auto_20170605_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='collaborator',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='client',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='collaborator',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
