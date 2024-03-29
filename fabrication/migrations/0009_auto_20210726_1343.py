# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-26 13:43
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('fabrication', '0008_auto_20210726_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricationpage',
            name='fabrication_content',
            field=wagtail.wagtailcore.fields.StreamField((('title_text_image', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('title_text_imagelist', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'ul', 'ol', 'link'])), ('image_list', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))))))), ('item_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()))), icon='list-ul')), ('numbered_item_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()))), icon='list-ol')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()))),
        ),
    ]
