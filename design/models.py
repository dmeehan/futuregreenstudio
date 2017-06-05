from __future__ import unicode_literals

from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class DesignPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('project_categories', label="Project Categories"),
    ]

    subpage_types = ['design.ProjectPage']

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(DesignPage, cls).can_create_at(parent) \
            and not cls.objects.exists()

class ProjectPageTag(TaggedItemBase):
    content_object = ParentalKey('ProjectPage', related_name='tagged_items')


class Collaborator(Orderable):
    page = ParentalKey('ProjectPage', related_name='collaborators')
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),  
    ]

    def __str__(self):
        return self.name

class Client(Orderable):
    page = ParentalKey('ProjectPage', related_name='clients')
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),  
    ]

    def __str__(self):
        return self.name

class ProjectPage(Page):    
    main_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+'
    )
    location = models.CharField(blank=True,
        max_length=255, help_text='Project location')
    description = RichTextField(blank=True)
    date = models.DateField("Project date")
    size = models.CharField(blank=True,
        max_length=255, help_text='Project size')

    categories = ParentalManyToManyField('design.ProjectCategory', blank=True)
    tags = ClusterTaggableManager(through=ProjectPageTag, blank=True)

    
    website = models.URLField(blank=True,
        help_text='Website URL')
    twitter = models.CharField(blank=True,
        max_length=255, help_text='Twitter username, without the @')
    facebook = models.URLField(blank=True,
        help_text='Facebook page URL')
    instagram = models.CharField(blank=True,
        max_length=255, help_text='Instagram username, without the @')

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('date'),
        FieldPanel('size'),
        FieldPanel('location'),
        FieldPanel('description'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        InlinePanel('clients', label="Clients"),
        InlinePanel('collaborators', label="Collaborators"),
        InlinePanel('gallery_images', label="Gallery images"),
        MultiFieldPanel([
            FieldPanel('website'),
            FieldPanel('twitter'),
            FieldPanel('facebook'),
            FieldPanel('instagram'),
        ], heading="External Links"),
    ]

    class Meta:
        verbose_name = "Project"


class ProjectPageGalleryImage(Orderable):
    page = ParentalKey(ProjectPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

from wagtail.wagtailsnippets.models import register_snippet

class ProjectCategory(Orderable, models.Model):
    page = ParentalKey(DesignPage, related_name='project_categories')
    name = models.CharField(max_length=255)
    
    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'project categories'