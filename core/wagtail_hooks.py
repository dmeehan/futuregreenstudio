from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html

from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('css/admin.css')
    )



@hooks.register('insert_editor_js')
def editor_js():

    return """

        <script>

            halloPlugins = {

                'halloformat': {},

                //'halloheadings': {formatBlocks: [h3, h4]},

                'hallolists': {},

                //'hallohr': {},

                'halloreundo': {},

                'hallowagtaillink': {},

                'hallorequireparagraphs': {},

            };

        </script>

    """

@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
  menu_items[:] = [item for item in menu_items if item.name != 'snippets']