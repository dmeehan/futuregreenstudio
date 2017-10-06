from __future__ import absolute_import, unicode_literals

from django.db import models
from django import forms

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.fields import ParentalKey

# general sitewide settings
@register_setting
class FirmInformation(BaseSetting):
    name = models.CharField(
        max_length=255, help_text='Firm name')
    tagline = models.CharField(
        max_length=255, help_text='Firm tagline')
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True,
        help_text='Email address to display on site.')
    phone = models.CharField(max_length=255, blank=True,
        help_text='Phone number to display on site.')
    fax = models.CharField(max_length=255, blank=True,
        help_text='Fax number to display on site.')
    twitter = models.CharField(
        max_length=255, blank=True, help_text='Twitter username, without the @')
    facebook = models.URLField(blank=True,
        help_text='Facebook page URL')
    instagram = models.CharField(blank=True,
        max_length=255, help_text='Instagram username, without the @')
    
    panels = [
        FieldPanel('name'),
        FieldPanel('tagline'),
        FieldPanel('address_1'),
        FieldPanel('address_2'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('zip_code'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('fax'),
        FieldPanel('twitter'),
        FieldPanel('facebook'),
        FieldPanel('instagram'),
    ]

@register_setting
class Mapbox(BaseSetting):
    map_tile_url = models.URLField()
    
    panels = [
        FieldPanel('map_tile_url'),
    ]

class HomePageGalleryItem(Orderable):
    THEME_CHOICES = (
        ('dark', 'Dark'),
        ('light', 'Light'),
    )
    
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        help_text='Add if you want this item to link to a page on this site.'
    )
    caption = RichTextField(features=['bold', 'italic'])
    theme = models.CharField(max_length=255, choices=THEME_CHOICES, default='light')
    page = ParentalKey('home.HomePage', related_name='slideshow_images')

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        FieldPanel('theme'),
        PageChooserPanel('link_page'),
    ]

class HomePage(Page):
    class Meta:
        verbose_name = "Homepage"

    subpage_types = ['design.DesignPage', 'profile.ProfilePage', 'contact.ContactPage', 'press.PressPage', 'research.ResearchPage', 'fabrication.FabricationPage']
    parent_page_types = []

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(HomePage, cls).can_create_at(parent) \
            and not cls.objects.exists()

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel('slideshow_images', label="Slideshow images"),
]

HomePage.promote_panels = Page.promote_panels