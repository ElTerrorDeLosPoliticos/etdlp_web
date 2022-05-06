from rest_framework import viewsets
from rest_framework_datatables.filters import DatatablesFilterBackend

from etdlp_app.serializers import PerfilSerializer
from legacy.models import ProveedoresBuscadorUtf


class ProveedoresViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PerfilSerializer
    filter_backends = [DatatablesFilterBackend, ]

    queryset = ProveedoresBuscadorUtf.objects.all().order_by('ruc')
    permission_classes = []
