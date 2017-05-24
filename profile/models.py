from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock, CharBlock, RichTextBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.fields import ParentalKey

@register_snippet
@python_2_unicode_compatible
class Collaborator(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),  
    ]

    def __str__(self):
        return self.name

@register_snippet
@python_2_unicode_compatible
class Client(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),  
    ]

    def __str__(self):
        return self.name

@register_snippet
@python_2_unicode_compatible
class Employee(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('title'), 
        FieldPanel('bio'), 
        ImageChooserPanel('image'),
    ]

    def __str__(self):
        return self.name


class ProfilePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+'
    )
    about_title = models.CharField(max_length=255)
    about_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('about_title'),
        FieldPanel('about_text'),
        InlinePanel('profile_employees', label="Employees"),
        InlinePanel('profile_clients', label="Clients"),
        InlinePanel('profile_collaborators', label="Collaborators"),
    ]

    subpage_types = []

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(ProfilePage, cls).can_create_at(parent) \
            and not cls.objects.exists()

class ProfilePageClient(Orderable, models.Model):
    page = ParentalKey(ProfilePage, related_name='profile_clients')
    client = models.ForeignKey('profile.Client', related_name='+')

    panels = [
        SnippetChooserPanel('client'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.client.name

class ProfilePageCollaborator(Orderable, models.Model):
    page = ParentalKey(ProfilePage, related_name='profile_collaborators')
    collaborator = models.ForeignKey('profile.Collaborator', related_name='+')

    panels = [
        SnippetChooserPanel('collaborator'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.collaborator.name

class ProfilePageEmployee(Orderable, models.Model):
    page = ParentalKey(ProfilePage, related_name='profile_employees')
    employee = models.ForeignKey('profile.Employee', related_name='+')

    panels = [
        SnippetChooserPanel('employee'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.employee.name
    

