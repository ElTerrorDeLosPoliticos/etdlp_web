from rest_framework import viewsets
from rest_framework import filters
from rest_framework_datatables.filters import DatatablesFilterBackend

from etdlp_app.serializers import PerfilSerializer, \
    ReporteContratosSerializer, ReporteEmpresasSerializer, ReporteSancionesSerializer
from legacy.models import ProveedoresBuscadorUtf, \
    AnalysisEmpresasSancionadasContratadoras, AnalysisContratosEmpresasInhabilitadas, AnalysisContratosDuranteSancion


class BaseViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [DatatablesFilterBackend, ]
    permission_classes = []


class ProveedoresViewSet(BaseViewSet):
    serializer_class = PerfilSerializer
    queryset = ProveedoresBuscadorUtf.objects.all()


class ProveedoresAPIViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PerfilSerializer
    queryset = ProveedoresBuscadorUtf.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['ruc', 'razon_social', 'organos_nomb_apell', 'organos_nrodocumento', 'representantes_nomb_apell', 'representantes_nrodocumento', 'socios', 'socios_dni']
    permission_classes = []


class ReporteContratosViewSet(BaseViewSet):
    serializer_class = ReporteContratosSerializer
    queryset = AnalysisContratosEmpresasInhabilitadas.objects.all()


class ReporteEmpresasViewSet(BaseViewSet):
    serializer_class = ReporteEmpresasSerializer
    queryset = AnalysisContratosDuranteSancion.objects.all()


class ReporteSancionesViewSet(BaseViewSet):
    serializer_class = ReporteSancionesSerializer
    queryset = AnalysisEmpresasSancionadasContratadoras.objects.all()
