# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.blocks import CharBlock, RichTextBlock, StreamBlock, BlockQuoteBlock, ListBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from core.blocks import CaptionedImageBlock, TitleAndTextBlock


class FabricationStreamBlock(StreamBlock):
    item_list = ListBlock(TitleAndTextBlock(), icon='list-ul')
    numbered_item_list = ListBlock(TitleAndTextBlock(), icon='list-ol')
    paragraph = RichTextBlock(icon="pilcrow")
    image = ImageChooserBlock()
    video = EmbedBlock()

class FabricationPage(Page):
    process_title = models.CharField(max_length=255)
    process_content = StreamField(FabricationStreamBlock())
    fabrication_title = models.CharField(max_length=255)
    fabrication_content = StreamField(FabricationStreamBlock())
    production_title = models.CharField(max_length=255)
    production_content = RichTextField()

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('process_title'),
                StreamFieldPanel('process_content'),
            ],
            heading="Process",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('fabrication_title'),
                InlinePanel('gallery_images', label="Slideshow image"),
                StreamFieldPanel('fabrication_content'),
            ],
            heading="Fabrication",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('production_title'),
                FieldPanel('production_content'),
            ],
            heading="Production",
            classname="collapsible"
        ),
    ]
        
        

    parent_page_types = ['home.HomePage']
    subpage_types = []

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(FabricationPage, cls).can_create_at(parent) \
            and not cls.objects.exists()

class FabricationPageGalleryImage(Orderable):
    page = ParentalKey(FabricationPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+', help_text="Minimum 1600px wide & 608px tall"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]