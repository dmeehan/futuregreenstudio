# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 20:54
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0005_auto_20170522_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitempage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'image_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.TextBlock(required=False))]), icon='image', label='Slideshow')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock()), (b'pullquote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'image_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.TextBlock(required=False))]), icon='image', label='Slideshow')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock()), (b'pullquote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
    ]
