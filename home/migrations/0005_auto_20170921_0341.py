# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 03:41
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170920_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagegalleryitem',
            name='caption',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
    ]