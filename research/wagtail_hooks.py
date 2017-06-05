from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import ResearchPage, ResearchProjectPage


class ResearchPageModelAdmin(ModelAdmin):
    model = ResearchPage
    menu_icon = 'folder-open-inverse'
    menu_order = 500
    add_to_settings_menu = False
    exclude_from_explorer = False

class ResearchProjectPageModelAdmin(ModelAdmin):
    model = ResearchProjectPage
    menu_icon = 'folder-open-inverse'
    menu_order = 500
    add_to_settings_menu = False
    exclude_from_explorer = False

class ResearchAdminGroup(ModelAdminGroup):
    menu_label = 'Research'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 700
    items = (ResearchProjectPageModelAdmin,)

#modeladmin_register(ResearchAdminGroup)