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


class ProfilePageClient(Orderable, models.Model):
    page = ParentalKey('profile.ProfilePage', related_name='clients')
    client = models.ForeignKey('design.Client', related_name='+')

    def __str__(self):
        return self.page.title + " -> " + self.client.name

class ProfilePageCollaborator(Orderable, models.Model):
    page = ParentalKey('profile.ProfilePage', related_name='collaborators')
    collaborator = models.ForeignKey('design.Collaborator', related_name='+')

    def __str__(self):
        return self.page.title + " -> " + self.collaborator.name


class EmployeePage(Page):
    job_title = models.CharField(max_length=255)
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('job_title'), 
        FieldPanel('bio'), 
        ImageChooserPanel('image'),
    ]

    subpage_types = []
    parent_page_types = ['profile.ProfilePage']

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
        InlinePanel('clients', label="Clients"),
        InlinePanel('collaborators', label="Collaborators"),
    ]

    subpage_types = ['profile.EmployeePage']
    parent_page_types = ['home.HomePage']

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(ProfilePage, cls).can_create_at(parent) \
            and not cls.objects.exists()

    def get_context(self, request):
        context = super(ProfilePage, self).get_context(request)
        employees = EmployeePage.objects.live().child_of(self)

        # make the variable 'employees' available on the template
        context['employees'] = employees

        return context

'''class ProfilePageEmployee(Orderable, models.Model):
    page = ParentalKey(ProfilePage, related_name='profile_employees')
    employee = models.ForeignKey('profile.Employee', related_name='+')

    panels = [
        SnippetChooserPanel('employee'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.employee.name'''
    

