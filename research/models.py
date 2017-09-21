from __future__ import unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from press.models import PublicationPage


class ResearchPage(Page):
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['research.ResearchProjectPage']

    def get_context(self, request):
        pagination_num = 3
        context = super(ResearchPage, self).get_context(request)
        
        all_projects = ResearchProjectPage.objects.live().child_of(self)

        publications = PublicationPage.objects.live()[:2]

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

        # make the variable 'projects' available on the template
        context['projects'] = projects
        context['publications'] = publications
        
        return context

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(ResearchPage, cls).can_create_at(parent) \
            and not cls.objects.exists()

class ResearchProjectPageTag(TaggedItemBase):
    content_object = ParentalKey('ResearchProjectPage', related_name='tagged_items')

class ResearchProjectPage(Page):
    date = models.DateField("Project date")
    description = RichTextField(features=['bold', 'italic', 'ul', 'ol', 'link'])
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


