from django.contrib.staticfiles.templatetags.staticfiles import static
from django.forms import Media, widgets

from wagtail.utils.widgets import WidgetWithScript

class MarkdownWidget(WidgetWithScript, widgets.Textarea):

    def render_js_init(self, id_, name, value):
        jsinit = """
            if (window.SimpleMDEInstances == null) {{
                window.SimpleMDEInstances = [];
            }}
            sm = new SimpleMDE({{
                element: document.getElementById("{id!s}"),
                forceSync: true,
                spellChecker: false
            }});
            window.SimpleMDEInstances.push(sm);
        """
        return jsinit.format(id=id_)

    @property
    def media(self):
        js = [
            static('vendor/simplemde/js/simplemde.min.js'),
        ]
        css = {'all': [
            static('vendor/simplemde/css/simplemde.min.css'),
        ]}

        return Media(js=js, css=css)