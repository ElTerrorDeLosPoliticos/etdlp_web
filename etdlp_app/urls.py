from etdlp_app import views
from django.urls import path, include
from rest_framework import routers

from etdlp_app import view_sets

router = routers.DefaultRouter()
router.register(r'proveedores', view_sets.ProveedoresViewSet, basename='api_proveedores')
router.register(r'reporte-contratos', view_sets.ReporteContratosViewSet, basename='api_reporte-contratos')
router.register(r'reporte-empresas', view_sets.ReporteEmpresasViewSet, basename='api_reporte-empresas')
router.register(r'reporte-sanciones', view_sets.ReporteSancionesViewSet, basename='api_reporte-sanciones')

busq_proveedores = [
    path('', views.buscador_proveedores, name='buscador_proveedores'),
    path('resultados/', views.resultado_proveedores, name='resultado_proveedores'),
]

reportes = [
    # path('', views.buscador_reportes, name='buscador_reportes'),
    path('', views.resultado_reportes, name='resultado_reportes'),
]
buscador_patterns = [
    path('perfiles/', views.buscador_perfiles, name='buscador_perfiles'),
    path('proveedores/', include(busq_proveedores)),
    path('reportes/<tabla>/', include(reportes)),
]

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('perfil/<ruc>', views.perfil_empresa, name='perfil_empresa'),
    path('buscador/', include(buscador_patterns)),
    path('api/', include(router.urls))
]
