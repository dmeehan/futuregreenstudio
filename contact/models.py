# contact/models
from __future__ import absolute_import

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.fields import ParentalKey


class ContactPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+', help_text="Minimum 1600px wide & 608px tall"
    )
    job_posting = RichTextField(features=['bold', 'italic', 'link'], blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
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