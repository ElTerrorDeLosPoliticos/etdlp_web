from django.contrib.postgres.aggregates import ArrayAgg, StringAgg
from django.db import models
from django.db.models import Count, Q, Case, When, Value, F, Subquery, OuterRef
from django.db.models.functions import Concat
from rest_framework import viewsets
from django_filters import filters
from rest_framework_datatables.django_filters.backends import DatatablesFilterBackend
from rest_framework_datatables.django_filters.filterset import DatatablesFilterSet
from rest_framework_datatables.django_filters.filters import GlobalFilter

from legacy.models import ProveedoresBuscadorUtf
from etdlp_app.serializers import PerfilSerializer


class GlobalCharFilter(GlobalFilter, filters.CharFilter):
    pass


class PerfilesEmpresaFilter(DatatablesFilterSet):
    """Filter name, artist and genre by name with icontains"""

    ruc = GlobalCharFilter(field_name='ruc', lookup_expr='icontains')
    razon_social = GlobalCharFilter(field_name='razon_social', lookup_expr='icontains')

    class Meta:
        model = ProveedoresBuscadorUtf
        fields = ['ruc', 'razon_social']


class PerfilesEmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PerfilSerializer
    filter_backends = [DatatablesFilterBackend, ]
    queryset = ProveedoresBuscadorUtf.objects.all().order_by('ruc')
    permission_classes = []
    filterset_class = PerfilesEmpresaFilter
