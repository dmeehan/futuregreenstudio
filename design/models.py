from __future__ import unicode_literals

from django import forms
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        InlinePanel('placeholder_images', label="Placeholder images"),
    ]

    subpage_types = ['design.ProjectPage']
    parent_page_types = ['home.HomePage']

    def get_context(self, request):
        pagination_num = 48
        context = super(DesignPage, self).get_context(request)
        
        category = request.GET.get('category')

        if category:
            context['search_category'] = category
            all_projects = ProjectPage.objects.live().child_of(self).filter(categories__name=category)
        else:
            all_projects = ProjectPage.objects.live().child_of(self)

        paginator = Paginator(all_projects, pagination_num)

        page = request.GET.get('page')
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            projects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            projects = paginator.page(paginator.num_pages)

        placeholders_xlarge = 4 - ((projects.object_list.count() + 1) % 4)
        placeholders_large = 3 - ((projects.object_list.count() + 1) % 3)
        placeholder_count_xlarge = 0 if placeholders_xlarge == 4 else placeholders_xlarge
        placeholder_count_large = 0 if placeholders_large == 3 else placeholders_large

        # make the variable 'projects' available on the template
        context['projects'] = projects
        context['placeholder_count_xlarge'] = placeholder_count_xlarge
        context['placeholder_count_large'] = placeholder_count_large

        return context


    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(DesignPage, cls).can_create_at(parent) \
            and not cls.objects.exists()

class DesignPagePlaceholderImage(Orderable):
    page = ParentalKey(DesignPage, related_name='placeholder_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        help_text='Placeholder image.')

    panels = [
        ImageChooserPanel('image'),
    ]

class ProjectPageTag(TaggedItemBase):
    content_object = ParentalKey('ProjectPage', related_name='tagged_items')


@register_snippet
class Collaborator(Orderable):
    page = ParentalKey('ProjectPage', related_name='collaborators', blank=True, null=True)
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),  
    ]

    def __str__(self):
        return self.name

@register_snippet
class Client(Orderable):
    page = ParentalKey('ProjectPage', related_name='clients', blank=True, null=True)
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
    list_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        blank=True, null=True
    )
    location = models.CharField(blank=True,
        max_length=255, help_text='Project location')
    description = RichTextField(features=['bold', 'italic', 'ul', 'ol', 'link'])
    date = models.CharField(blank=True,
        max_length=255, help_text='Project Date / Season')
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
        ImageChooserPanel('list_image'),
        FieldPanel('date'),
        FieldPanel('size'),
        FieldPanel('location'),
        FieldPanel('description'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        InlinePanel('clients', label="Clients"),
        InlinePanel('collaborators', label="Collaborators"),
        InlinePanel('gallery_images', label="Slideshow images"),
        InlinePanel('videos', label="Videos"),
        MultiFieldPanel([
            FieldPanel('website'),
            FieldPanel('twitter'),
            FieldPanel('facebook'),
            FieldPanel('instagram'),
        ], heading="External Links"),
    ]

    subpage_types = []
    parent_page_types = ['design.DesignPage']

    class Meta:
        verbose_name = "Project"


class ProjectPageGalleryImage(Orderable):
    page = ParentalKey(ProjectPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', blank=True, null=True, on_delete=models.PROTECT, related_name='+',
        help_text='Slideshow image.')
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class ProjectPageVideo(Orderable):
    page = ParentalKey(ProjectPage, related_name='videos')
    video = models.URLField(blank=True,
        help_text='URL from a video streaming service such as Vimeo.')
    panels = [
        FieldPanel('video'),
    ]


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