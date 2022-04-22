import inspect

from django.contrib import admin
from legacy import models as legacy_models


# Register your models here.


class ReadOnlyAdminDisplay(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def __init__(self, model, admin_site):
        self.list_display = ['index']
        self.list_display += [field.name for field in model._meta.fields if field.name != "index"]

        super(ReadOnlyAdminDisplay, self).__init__(model, admin_site)


classes = [obj
           for _, obj in inspect.getmembers(legacy_models, predicate=inspect.isclass)]

for class_ in classes:
    admin.site.register(class_, ReadOnlyAdminDisplay)
