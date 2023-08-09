# contact/models
from __future__ import absolute_import

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.blocks import ListBlock, StreamBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.fields import ParentalKey

from core.blocks import TwoImageBlock, CaptionedImageBlock

class ContactStreamBlock(StreamBlock):
    two_images = TwoImageBlock()
    image = ImageChooserBlock(template='press/blocks/image.html')
    image_gallery = ListBlock(CaptionedImageBlock(), icon="image", label="Image Slideshow")
    video = EmbedBlock()

class ContactPage(Page):
    body = StreamField(ContactStreamBlock(required=False), blank=True, null=True, help_text='Page Content')
    job_posting = RichTextField(features=['bold', 'italic', 'link'], blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        FieldPanel('job_posting'),
    ]

    subpage_types = []

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(ContactPage, cls).can_create_at(parent) \
            and not cls.objects.exists()

@register_setting
class Mailchimp(BaseSetting):
    subscribe_url = models.URLField()
    
    panels = [
        FieldPanel('subscribe_url'),
    ]