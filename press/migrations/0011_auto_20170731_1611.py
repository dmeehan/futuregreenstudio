# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 16:11
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0010_publicationpagerelatedlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitempage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='press/blocks/image.html')), (b'image_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.TextBlock(required=False))]), icon='image', label='Slideshow')), (b'image_or_video_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock())]), icon='image', label='Slideshow')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock()), (b'project', wagtail.wagtailcore.blocks.PageChooserBlock(target_model=['design.ProjectPage'], template='design/blocks/related_project.html')), (b'pullquote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='press/blocks/image.html')), (b'image_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.TextBlock(required=False))]), icon='image', label='Slideshow')), (b'image_or_video_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock())]), icon='image', label='Slideshow')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock()), (b'project', wagtail.wagtailcore.blocks.PageChooserBlock(target_model=['design.ProjectPage'], template='design/blocks/related_project.html')), (b'pullquote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
    ]
