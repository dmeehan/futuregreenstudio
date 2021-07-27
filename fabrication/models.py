# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.db import models

from django.utils.encoding import python_2_unicode_compatible

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.wagtailcore.blocks import CharBlock, RichTextBlock, StreamBlock, BlockQuoteBlock, ListBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from core.blocks import CaptionedImageBlock, TitleAndTextBlock, TitleTextImageBlock, TitleTextImageListBlock


class FabricationStreamBlock(StreamBlock):
    title_text_image = TitleTextImageBlock()
    title_text_imagelist = TitleTextImageListBlock()
    item_list = ListBlock(TitleAndTextBlock(), icon='list-ul')
    numbered_item_list = ListBlock(TitleAndTextBlock(), icon='list-ol')
    paragraph = RichTextBlock(icon="pilcrow")
    image = ImageChooserBlock()
    video = EmbedBlock()

class FabricationPage(Page):
    video_hd_url = models.URLField(blank=True,
        help_text='High Definition URL from a video streaming service such as Vimeo.')
    video_sd_url = models.URLField(blank=True,
        help_text='Standard Definition URL from a video streaming service such as Vimeo.')
    video_poster = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        blank=True, null=True, help_text="Still frame from video to show while loading"
    )
    fabrication_content = StreamField(FabricationStreamBlock())
    

    content_panels = Page.content_panels + [
        FieldPanel('video_hd_url'),
        FieldPanel('video_sd_url'),
        ImageChooserPanel('video_poster'),
        StreamFieldPanel('fabrication_content'),
    ]
        
    parent_page_types = ['home.HomePage'] 
    subpage_types = ['fabrication.FabricationMaterialPage']

    def get_context(self, request):
        context = super(FabricationPage, self).get_context(request)
        materials = FabricationMaterialPage.objects.live().child_of(self)

        # make the variable 'Materials' available on the template
        context['materials'] = materials

        return context

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(FabricationPage, cls).can_create_at(parent) \
            and not cls.objects.exists()

class FabricationProjectPage(Page):    
    list_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        blank=True, null=True, help_text="Minimum 800px wide & 800px tall"
    )
    
    description = RichTextField(features=['bold', 'italic', 'ul', 'ol', 'link'])
    items = models.CharField(blank=True, max_length=250)

    content_panels = Page.content_panels + [
        
        ImageChooserPanel('list_image'),
        FieldPanel('description'),
        FieldPanel('items'),
        InlinePanel('fabrication_project_gallery_images', label="Slideshow images"),
    ]

    subpage_types = []
    parent_page_types = ['fabrication.FabricationMaterialPage']

    class Meta:
        verbose_name = "Fabrication Project"

class FabricationMaterialPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        help_text='Material Image', blank=True, null=True)
    
    content_panels = Page.content_panels + [
       ImageChooserPanel('image'),
    ]

    subpage_types = ['fabrication.FabricationProjectPage']
    parent_page_types = ['fabrication.FabricationPage']

    def get_context(self, request):
        context = super(FabricationMaterialPage, self).get_context(request)
        projects = FabricationProjectPage.objects.live().child_of(self)

        # make the variable 'Materials' available on the template
        context['projects'] = projects

        return context

    class Meta:
        verbose_name_plural = 'fabrication materials'

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

class FabricationProjectPageGalleryImage(Orderable):
    page = ParentalKey(FabricationProjectPage, related_name='fabrication_project_gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+', help_text="Minimum 1600px wide & 608px tall"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
