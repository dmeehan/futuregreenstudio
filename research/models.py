from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class ResearchPage(Page):
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['research.ResearchProjectPage']

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(ResearchPage, cls).can_create_at(parent) \
            and not cls.objects.exists()

class ResearchProjectPageTag(TaggedItemBase):
    content_object = ParentalKey('ResearchProjectPage', related_name='tagged_items')

class ResearchProjectPage(Page):
    date = models.DateField("Project date")
    description = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=ResearchProjectPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('description'),
        InlinePanel('gallery_images', label="Images"),
        InlinePanel('related_links', label="Related Links"),
    ]

    parent_page_types = ['research.ResearchPage']
    subpage_types = []

    class Meta:
        verbose_name = "Research Project"

class ResearchProjectPageGalleryImage(Orderable):
    page = ParentalKey(ResearchProjectPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class ResearchProjectPageRelatedLinks(Orderable):
    page = ParentalKey(ResearchProjectPage, related_name='related_links')
    title = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('url'),  
    ]

    def __str__(self):
        return self.title


