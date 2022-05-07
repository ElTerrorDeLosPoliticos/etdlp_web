from django.urls import reverse
from rest_framework import serializers
from legacy import models as legacy_models


class SocioSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='porcentajeacciones')
    name = serializers.CharField(source='razonsocial_socio')

    class Meta:
        model = legacy_models.ProveedoresPerfilSociosUtf
        fields = ['razon_social', 'name', 'sigladocide', 'nrodocumento', 'fechaingreso', 'value']
        # list_serializer_class = CustomListSerializer


class AdministrativosSerializer(serializers.ModelSerializer):
    class Meta:
        model = legacy_models.ProveedoresPerfilOrgAdministrativosCsv
        fields = ['apellidosnomb', 'sigladocide', 'nrodocumento', 'desccargo', 'desctipoorgano', 'fechaingreso']


class GeograficasSerializer(serializers.ModelSerializer):
    class Meta:
        model = legacy_models.ProveedoresPerfilInfoGeoUtf
        fields = ['departamento', 'provincia', 'distrito', 'estado', 'condicion', 'codigoregistro']


class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = legacy_models.ProveedoresPerfilSeaceUtf
        fields = ['nomentcont', 'descontprov', 'montoorigen', 'desestcontprov', 'descatobj2', 'codcontprov']


class ContratantesCountSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = legacy_models.ProveedoresPerfilSeaceUtf
        fields = ['nomentcont', 'total']


class TipoContratoCountSerializer(serializers.ModelSerializer):
    value = serializers.CharField()
    name = serializers.CharField(source='descatobj2')

    class Meta:
        model = legacy_models.ProveedoresPerfilSeaceUtf
        fields = ['name', 'value']


class SancionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = legacy_models.ProveedoresPerfilSancionesUtf
        fields = ['descripcion', 'motivos', 'fechaini_field', 'fechafin_field', 'meses_sancionado', 'vigente', 'montotexto', 'nrores']


"""
    Serializers para viewsets    
"""


class PerfilSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, instance):
        return reverse('perfil_empresa', kwargs={'ruc': instance.ruc})

    class Meta:
        model = legacy_models.ProveedoresBuscadorUtf
        fields = '__all__'


class ReporteContratosSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, instance):
        return reverse('perfil_empresa', kwargs={'ruc': instance.ruc})

    class Meta:
        model = legacy_models.AnalysisContratosEmpresasInhabilitadas
        fields = '__all__'


class ReporteEmpresasSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, instance):
        return reverse('perfil_empresa', kwargs={'ruc': instance.ruc})

    class Meta:
        model = legacy_models.AnalysisContratosDuranteSancion
        fields = '__all__'


class ReporteSancionesSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, instance):
        return reverse('perfil_empresa', kwargs={'ruc': instance.ruc})

    class Meta:
        model = legacy_models.AnalysisEmpresasSancionadasContratadoras
        fields = '__all__'
