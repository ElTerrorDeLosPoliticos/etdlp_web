from rest_framework import serializers
from legacy.models import *


# class CustomListSerializer(serializers.ListSerializer):
#     def to_representation(self, data):
#         iterable = data.all() if isinstance(data, models.Manager) else data
#         return [
#             (item.razonsocial_socio if isinstance(self.child, SocioSerializer) else item.id, self.child.to_representation(item)) for item in iterable
#         ]
#
#     @property
#     def data(self):
#         ret = super(CustomListSerializer, self).data
#         return serializers.ReturnDict(ret, serializer=self)


class SocioSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='porcentajeacciones')
    name = serializers.CharField(source='razonsocial_socio')

    class Meta:
        model = ProveedoresPerfilSociosUtf
        fields = ['razon_social', 'name', 'sigladocide', 'nrodocumento', 'fechaingreso', 'value']
        # list_serializer_class = CustomListSerializer


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