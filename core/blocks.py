import markdown

from django import forms
from django.db import models
from django.utils.functional import cached_property

from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.wagtailcore.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock, PageChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.utils.widgets import WidgetWithScript

from .widgets import MarkdownWidget


class CaptionedImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)
 
    class Meta:
        icon = 'image'

    class Meta:
        template = 'core/blocks/captioned_image.html'

class TitleAndTextBlock(StructBlock):
    title = CharBlock()
    text = TextBlock()

    class Meta:
        template = 'core/blocks/title_and_text.html'

class CarouselBlock(StreamBlock):
    image = ImageChooserBlock()
    video = EmbedBlock()

    class Meta:
        icon='cogs'

class TwoColumnBlock(TextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'core/blocks/two_column.html'


class MarkdownBlock(TextBlock):
    @cached_property
    def field(self):
        field_kwargs = {
            'widget': MarkdownWidget(),
        }
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)

    class Meta:
        icon = 'pilcrow'
        template = 'core/blocks/markdown.html'
