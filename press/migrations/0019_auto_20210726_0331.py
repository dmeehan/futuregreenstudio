# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-26 03:31
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0018_auto_20171006_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitempage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'ul', 'ol', 'link'], icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='press/blocks/image.html')), ('image_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)))), icon='image', label='Image Slideshow')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('project', wagtail.wagtailcore.blocks.PageChooserBlock(target_model=['design.ProjectPage'], template='design/blocks/related_project.html')), ('pullquote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))), blank=True, help_text='Content for FGS published articles. Optional', null=True),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'ul', 'ol', 'link'], icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='press/blocks/image.html')), ('image_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)))), icon='image', label='Image Slideshow')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('project', wagtail.wagtailcore.blocks.PageChooserBlock(target_model=['design.ProjectPage'], template='design/blocks/related_project.html')), ('pullquote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')))),
        ),
    ]
