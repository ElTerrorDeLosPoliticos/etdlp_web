from django.urls import reverse
from rest_framework import serializers
from legacy.models import *


class SocioSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='porcentajeacciones')
    name = serializers.CharField(source='razonsocial_socio')

    class Meta:
        model = ProveedoresPerfilSociosUtf
        fields = ['razon_social', 'name', 'sigladocide', 'nrodocumento', 'fechaingreso', 'value']
        # list_serializer_class = CustomListSerializer


class AdministrativosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedoresPerfilOrgAdministrativosCsv
        fields = ['apellidosnomb', 'sigladocide', 'nrodocumento', 'desccargo', 'desctipoorgano', 'fechaingreso']


class GeograficasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedoresPerfilInfoGeoUtf
        fields = ['departamento', 'provincia', 'distrito', 'estado', 'condicion', 'codigoregistro']


class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedoresPerfilSeaceUtf
        fields = ['nomentcont', 'descontprov', 'montoorigen', 'desestcontprov', 'descatobj2', 'codcontprov']


class ContratantesCountSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = ProveedoresPerfilSeaceUtf
        fields = ['nomentcont', 'total']


class TipoContratoCountSerializer(serializers.ModelSerializer):
    value = serializers.CharField()
    name = serializers.CharField(source='descatobj2')

    class Meta:
        model = ProveedoresPerfilSeaceUtf
        fields = ['name', 'value']


class SancionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedoresPerfilSancionesUtf
        fields = ['descripcion', 'motivos', 'fechaini_field', 'fechafin_field', 'meses_sancionado', 'vigente', 'montotexto', 'nrores']


class PerfilSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, instance):
        return reverse('perfil_empresa', kwargs={'ruc': instance.ruc})

    class Meta:
        model = ProveedoresBuscadorUtf
        fields = '__all__'
