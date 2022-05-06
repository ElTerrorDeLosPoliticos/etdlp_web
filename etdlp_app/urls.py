from etdlp_app import views
from django.urls import path, include
from rest_framework import routers

from etdlp_app import view_sets

router = routers.DefaultRouter()
router.register(r'proveedores', view_sets.ProveedoresViewSet, basename='api_proveedores')

buscador_patterns = [
    path('proveedores', views.buscador_proveedores, name='buscador_proveedores'),
    path('perfiles', views.buscador_perfiles, name='buscador_perfiles'),
    path('resultados', views.resultado_proveedores, name='resultado_proveedores'),
]

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('perfil/<ruc>', views.perfil_empresa, name='perfil_empresa'),
    path('buscador/', include(buscador_patterns)),
    path('api/', include(router.urls))
]
