# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0007_auto_20170731_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpagegalleryimage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Slideshow image. Include either one image or one video per slideshow item.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
    ]
