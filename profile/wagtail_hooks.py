from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import Employee, Client, Collaborator, ProfilePage


class ProfilePageModelAdmin(ModelAdmin):
    model = ProfilePage
    menu_icon = 'user'  # change as required
    menu_order = 500  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    #list_display = ('name', 'title')
    #search_fields = ('name',)


class EmployeeModelAdmin(ModelAdmin):
    model = Employee
    menu_icon = 'group'  # change as required
    menu_order = 500  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', 'title')
    search_fields = ('name',)

class ClientModelAdmin(ModelAdmin):
    model = Client
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 600  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name')
    search_fields = ('name',)

class CollaboratorModelAdmin(ModelAdmin):
    model = Collaborator
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 700  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name')
    search_fields = ('name',)

class ProfileAdminGroup(ModelAdminGroup):
    menu_label = 'Profile'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 500  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ClientModelAdmin, CollaboratorModelAdmin, EmployeeModelAdmin)

# Now you just need to register your customised ModelAdmin class with Wagtail
#modeladmin_register(EmployeeModelAdmin)
#modeladmin_register(ClientModelAdmin)
#modeladmin_register(CollaboratorModelAdmin)
modeladmin_register(ProfileAdminGroup)