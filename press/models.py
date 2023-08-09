from __future__ import unicode_literals
import calendar

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore.blocks import CharBlock, RichTextBlock, StreamBlock, BlockQuoteBlock, ListBlock, PageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsearch import index

from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route

from core.blocks import CaptionedImageBlock

@register_snippet
class Award(index.Indexed, models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField("Award date")
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('date'),
        FieldPanel('url'),  
    ]

    def __str__(self):
        return self.name

    class Meta:
        ordering  = ['-date',]

    search_fields = [
        index.SearchField('name', partial_match=True),
    ]

class PressStreamBlock(StreamBlock):
    heading = CharBlock(icon="title", classname="title")
    subheading = CharBlock(icon="title", classname="title")
    text = RichTextBlock(icon="pilcrow", features=['bold', 'italic', 'ul', 'ol', 'link'])
    image = ImageChooserBlock(template='press/blocks/image.html')
    image_gallery = ListBlock(CaptionedImageBlock(), icon="image", label="Image Slideshow")
    #image_or_video_gallery = ListBlock(CarouselBlock(), icon="image", label="Image or Video Slideshow")
    video = EmbedBlock()
    project = PageChooserBlock(target_model='design.ProjectPage', template='design/blocks/related_project.html')
    pullquote = BlockQuoteBlock()
    document = DocumentChooserBlock(icon="doc-full-inverse")


class PressPage(RoutablePageMixin, Page):

    placeholder_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+', null=True, blank=True,
        help_text='Press article placeholder image. Minimum 400px wide & 500px tall.')

    def get_context(self, request):
        context = super(PressPage, self).get_context(request)
        #publications = PublicationPage.objects.live().child_of(self)
        #all_newsitems = NewsItemPage.objects.live().child_of(self).order_by('-date')
        recent_newsitems = NewsItemPage.objects.live().child_of(self).order_by('-date')[:10]
        archive_dates = NewsItemPage.objects.live().dates('date', 'month', order='DESC')

        #paginator = Paginator(all_newsitems, 3) # Show 3 news items per page

        #page = request.GET.get('page')
        #try:
        #    newsitems = paginator.page(page)
        #except PageNotAnInteger:
            # If page is not an integer, deliver first page.
        #    newsitems = paginator.page(1)
        #except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
        #    newsitems = paginator.page(paginator.num_pages)

        # make the variable 'newsitems' available on the template
        context['recent_newsitems'] = recent_newsitems
        context['archive_dates'] = archive_dates
        #context['publications'] = publications

        return context
    

    content_panels = Page.content_panels + [
        InlinePanel('featured_news', label="Featured News Items"),
        ImageChooserPanel('placeholder_image'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['press.NewsItemPage']

    def get_newsitems(self):
        return NewsItemPage.objects.descendant_of(self).live().order_by('-date')

    @route(r'^archive/(\d{4})/$')
    @route(r'^archive/(\d{4})/(\d{2})/$')
    @route(r'^archive/(\d{4})/(\d{2})/(\d{2})/$')
    def archive(self, request, year, month=None, day=None, *args, **kwargs):
        self.newsitems = self.get_newsitems().filter(date__year=year)
        self.year = year
        if month:
            self.month = calendar.month_name[int(month)]
            self.newsitems = self.newsitems.filter(date__month=month)
        if day:
            self.day = day
            self.newsitems = self.newsitems.filter(date__day=day)
        return Page.serve(self, request, *args, **kwargs)

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(PressPage, cls).can_create_at(parent) \
            and not cls.objects.exists()
    
class PublicationPage(Page):
    body = StreamField(PressStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        InlinePanel('related_links', label="Related Links"),
    ]

    parent_page_types = []
    subpage_types = []

    class Meta:
        verbose_name = "Publication"

class NewsItemPage(Page):
    date = models.DateField("Post date")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+', null=True, blank=True,
        help_text="Teaser Image. Minimum 400px wide & 500px tall")
    external_link = models.URLField(null=True, blank=True, help_text='Link to article in external publication. Optional')
    publication_name = models.CharField(max_length=255, null=True, blank=True)
    body = StreamField(PressStreamBlock(required=False), blank=True, null=True, help_text='Content for FGS published articles. Optional')

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('image'),
        FieldPanel('external_link'),
        FieldPanel('publication_name'),
        StreamFieldPanel('body'),
    ]   

    parent_page_types = ['press.PressPage']
    subpage_types = []

    class Meta:
        verbose_name = "News Item"

    def get_context(self, request):
        context = super(NewsItemPage, self).get_context(request)
        recent_newsitems = NewsItemPage.objects.live().order_by('-date')[:10]
        archive_dates = NewsItemPage.objects.live().dates('date', 'month', order='DESC')

        context['recent_newsitems'] = recent_newsitems
        context['archive_dates'] = archive_dates

        return context

class FeaturedNewsItem(Orderable):
    page = ParentalKey(PressPage, related_name='featured_news')
    news_item = models.ForeignKey(NewsItemPage, related_name='+')


class PublicationPageRelatedLink(Orderable):
    page = ParentalKey(PublicationPage, related_name='related_links')
    title = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('url'),  
    ]

    def __str__(self):
        return self.title





