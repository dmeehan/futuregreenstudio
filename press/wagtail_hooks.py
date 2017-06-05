from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import Award, PublicationPage, NewsItemPage, PressPage


class PressPageModelAdmin(ModelAdmin):
    model = PressPage
    menu_icon = 'folder-open-inverse'
    menu_order = 500

class NewsItemPageModelAdmin(ModelAdmin):
    model = NewsItemPage
    menu_icon = 'folder-open-inverse'
    menu_order = 500

class AwardModelAdmin(ModelAdmin):
    model = Award
    menu_icon = 'folder-open-inverse'
    menu_order = 500 

class PublicationPageModelAdmin(ModelAdmin):
    model = PublicationPage
    menu_icon = 'folder-open-inverse'
    menu_order = 500

class PressAdminGroup(ModelAdminGroup):
    menu_label = 'Press'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 600  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (NewsItemPageModelAdmin, PublicationPageModelAdmin, AwardModelAdmin)


#modeladmin_register(PressAdminGroup)