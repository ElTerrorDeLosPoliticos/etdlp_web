from django.contrib import admin
# from legacy.models import PlanillaBuscadorUtf


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


# admin.site.register(PlanillaBuscadorUtf, ReadOnlyAdminDisplay)
# admin.site.register(PlanillaPerfilUtf, ReadOnlyAdminDisplay)
# admin.site.register(ProveedoresBuscadorUtf, ReadOnlyAdminDisplay)
# admin.site.register(ProveedoresPerfilInfoGeoUtf, ReadOnlyAdminDisplay)
# admin.site.register(ProveedoresPerfilOrgAdministrativosCsv, ReadOnlyAdminDisplay)
# admin.site.register(ProveedoresPerfilRepresentantesUtf, ReadOnlyAdminDisplay)
# admin.site.register(ProveedoresPerfilSancionesUtf, ReadOnlyAdminDisplay)
# admin.site.register(ProveedoresPerfilSeaceUtf, ReadOnlyAdminDisplay)
# admin.site.register(ProveedoresPerfilSociosUtf, ReadOnlyAdminDisplay)
# admin.site.register(VisitantesBuscadorUtf, ReadOnlyAdminDisplay)
# admin.site.register(VisitantesEmpresariosUtf, ReadOnlyAdminDisplay)
# admin.site.register(VisitantesPerfilUtf, ReadOnlyAdminDisplay)
