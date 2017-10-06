from __future__ import unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

#from press.models import PublicationPage
from core.blocks import BasicStreamBlock


class ResearchPage(Page):
    #intro = models.TextField()

    content_panels = Page.content_panels + [
        InlinePanel('featured_research_projects', label="Featured Research Projects"),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['research.ResearchProjectPage']

    def get_context(self, request):
        #pagination_num = 3
        context = super(ResearchPage, self).get_context(request)
        
        all_projects = ResearchProjectPage.objects.live().child_of(self).order_by('-date')

        #publications = PublicationPage.objects.live()[:2]
        #paginator = Paginator(all_projects, pagination_num)
        #page = request.GET.get('page')
        #try:
        #    projects = paginator.page(page)
        #except PageNotAnInteger:
            # If page is not an integer, deliver first page.
        #    projects = paginator.page(1)
        #except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
        #    projects = paginator.page(paginator.num_pages)

        # make the variable 'projects' available on the template
        context['projects'] = all_projects
        #context['publications'] = publications
        
        return context

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(ResearchPage, cls).can_create_at(parent) \
            and not cls.objects.exists()

class ResearchProjectPageTag(TaggedItemBase):
    content_object = ParentalKey('ResearchProjectPage', related_name='tagged_items')

class ResearchProjectPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        null=True, help_text="Minimum 1600px wide & 800px tall"
    )
    list_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        blank=True, null=True, help_text="Minimum 800px wide & 800px tall"
    )
    date = models.DateField("Project date")
    subtitle = StreamField(BasicStreamBlock(required=False), blank=True)
    description = RichTextField(features=['bold', 'italic', 'ul', 'ol', 'link'])
    additional_details = StreamField(BasicStreamBlock(required=False), blank=True)
    tags = ClusterTaggableManager(through=ResearchProjectPageTag, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        ImageChooserPanel('list_image'),
        FieldPanel('date'),
        FieldPanel('description'),
        StreamFieldPanel('subtitle'),
        StreamFieldPanel('additional_details'),
        InlinePanel('gallery_images', label="Images"),
        InlinePanel('videos', label="Videos"),
        InlinePanel('related_links', label="Related Links"),
    ]

    parent_page_types = ['research.ResearchPage']
    subpage_types = []

    class Meta:
        verbose_name = "Research Project"

class FeaturedResearchProject(Orderable):
    page = ParentalKey(ResearchPage, related_name='featured_research_projects')
    research_project = models.ForeignKey(ResearchProjectPage, related_name='+')


class ResearchProjectPageGalleryImage(Orderable):
    page = ParentalKey(ResearchProjectPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+', help_text="Minimum 1160px wide & 1160px tall"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class ResearchProjectPageVideo(Orderable):
    page = ParentalKey(ResearchProjectPage, related_name='videos')
    video = models.URLField(blank=True,
        help_text='URL from a video streaming service such as Vimeo.')
    panels = [
        FieldPanel('video'),
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


