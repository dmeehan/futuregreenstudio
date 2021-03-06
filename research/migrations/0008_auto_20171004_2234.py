# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 22:34
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0007_researchprojectpagevideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchprojectpage',
            name='additional_details',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(features=[b'bold', b'italic'], icon=b'pilcrow'))], blank=True),
        ),
        migrations.AlterField(
            model_name='researchprojectpage',
            name='subtitle',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(features=[b'bold', b'italic'], icon=b'pilcrow'))], blank=True),
        ),
    ]
