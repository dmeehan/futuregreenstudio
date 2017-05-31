from __future__ import unicode_literals

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
from wagtail.wagtailsearch import index

from core.blocks import CaptionedImageBlock, MarkdownBlock

class Award(models.Model):
    page = ParentalKey('press.PressPage', related_name='awards')
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

class PressStreamBlock(StreamBlock):
    heading = CharBlock(icon="title", classname="title")
    subheading = CharBlock(icon="title", classname="title")
    text = RichTextBlock(icon="pilcrow")
    image = ImageChooserBlock()
    image_gallery = ListBlock(CaptionedImageBlock(), icon="image", label="Slideshow")
    video = EmbedBlock()
    project = PageChooserBlock(target_model='design.ProjectPage', template = 'design/blocks/related_project.html')
    pullquote = BlockQuoteBlock()
    document = DocumentChooserBlock(icon="doc-full-inverse")


class PressPage(Page):

    def get_context(self, request):
        context = super(PressPage, self).get_context(request)
        all_newsitems = NewsItemPage.objects.live().child_of(self).order_by('-date')

        paginator = Paginator(all_newsitems, 5) # Show 5 resources per page

        page = request.GET.get('page')
        try:
            newsitems = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            newsitems = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            newsitems = paginator.page(paginator.num_pages)

        # make the variable 'newsitems' available on the template
        context['newsitems'] = newsitems

        return context
    
    #def get_context(self, request):
    #    context = super(PressPage, self).get_context(request)
    #    context['newsitems'] = self.get_children().type(NewsItemPage)
    #    return context

    content_panels = Page.content_panels + [
        InlinePanel('awards', label="Awards"),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['press.PublicationPage', 'press.NewsItemPage']

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(PressPage, cls).can_create_at(parent) \
            and not cls.objects.exists()
    
class PublicationPage(Page):
    body = StreamField(PressStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['press.PressPage']
    subpage_types = []

    class Meta:
        verbose_name = "Publication"

class NewsItemPage(Page):
    date = models.DateField("Post date")
    body = StreamField(PressStreamBlock())

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['press.PressPage']
    subpage_types = []

    class Meta:
        verbose_name = "News Item"





