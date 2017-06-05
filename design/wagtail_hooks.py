from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import DesignPage, ProjectPage


class DesignPageModelAdmin(ModelAdmin):
    model = DesignPage
    menu_icon = 'folder-open-inverse'
    menu_order = 500
    add_to_settings_menu = False
    exclude_from_explorer = False

class ProjectPageModelAdmin(ModelAdmin):
    model = ProjectPage
    menu_icon = 'folder-open-inverse'
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False

class DesignAdminGroup(ModelAdminGroup):
    menu_label = 'Design'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 700
    items = (ProjectPageModelAdmin,)

#modeladmin_register(DesignAdminGroup)