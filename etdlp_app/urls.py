from etdlp_app import views
from django.urls import path, include

buscador_patterns = [
    path('proveedores', views.buscador_proveedores, name='perfil_empresa'),
    path('perfiles', views.buscador_perfiles, name='buscador_perfiles'),
    path('resultados', views.resultado_proveedores, name='resultado_proveedores'),
]

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('perfil/<ruc>', views.perfil_empresa, name='perfil_empresa'),
    path('buscador/', include(buscador_patterns)),
]
