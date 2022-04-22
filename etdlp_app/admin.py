from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from etdlp_app.models import Usuario

UserAdmin.list_filter += ('borrado',)
UserAdmin.list_display += ('borrado',)
UserAdmin.fieldsets[0][1]['fields'] += ('borrado',)
admin.site.register(Usuario, UserAdmin)
