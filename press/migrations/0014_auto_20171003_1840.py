# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('press', '0013_auto_20170925_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedNewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='newsitempage',
            name='external_link',
            field=models.URLField(blank=True, help_text='Link to article in external publication. Optional', null=True),
        ),
        migrations.AddField(
            model_name='newsitempage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Teaser image.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='newsitempage',
            name='publication_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newsitempage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(features=['bold', 'italic', 'ul', 'ol', 'link'], icon='pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='press/blocks/image.html')), (b'image_gallery', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.TextBlock(required=False))]), icon='image', label='Image Slideshow')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock()), (b'project', wagtail.wagtailcore.blocks.PageChooserBlock(target_model=['design.ProjectPage'], template='design/blocks/related_project.html')), (b'pullquote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))], help_text='Content for FGS published articles. Optional'),
        ),
        migrations.AddField(
            model_name='featurednewsitem',
            name='news_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='press.NewsItemPage'),
        ),
        migrations.AddField(
            model_name='featurednewsitem',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_news', to='press.PressPage'),
        ),
    ]