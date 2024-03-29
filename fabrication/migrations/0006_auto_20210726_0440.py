# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-26 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('fabrication', '0005_auto_20210726_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fabricationcategory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='fabricationcategory',
            name='page',
        ),
        migrations.AlterModelOptions(
            name='fabricationmaterialpage',
            options={'verbose_name_plural': 'fabrication materials'},
        ),
        migrations.RemoveField(
            model_name='fabricationprojectpage',
            name='categories',
        ),
        migrations.AddField(
            model_name='fabricationmaterialpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Placeholder image.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='fabricationmaterialpage',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='FabricationCategory',
        ),
    ]
