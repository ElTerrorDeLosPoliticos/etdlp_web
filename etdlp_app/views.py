from django.db.models import Count, Q, Sum
from django.shortcuts import render, redirect
from etdlp_app.serializers import *
import json


# Create your views here.
def main_page(request):
    return render(request, 'index.html', {})


def perfil_empresa(request, ruc):
    try:
        empresa = ProveedoresBuscadorUtf.objects.get(ruc=ruc)

        socios = ProveedoresPerfilSociosUtf.objects.filter(ruc=ruc)
        socios_serial = SocioSerializer(socios, many=True).data

        represents = ProveedoresPerfilRepresentantesUtf.objects.filter(ruc=ruc)

        contratantes_count = ProveedoresPerfilSeaceUtf.objects.filter(ruc=ruc).values('nomentcont').annotate(total=Count('razon_social', filter=Q(ruc=ruc)))
        contratantes_count_serial = ContratantesCountSerializer(contratantes_count, many=True).data

        contratos = ProveedoresPerfilSeaceUtf.objects.filter(ruc=ruc)

        tipocontratos_count = ProveedoresPerfilSeaceUtf.objects.values('descatobj2').annotate(value=Count('descatobj2', filter=Q(ruc=ruc))).order_by('descatobj2')
        tipocontratos_count_serial = TipoContratoCountSerializer(tipocontratos_count, many=True).data

        context = {
            'empresa': empresa,
            'socios_chart': json.dumps(socios_serial),
            'socios_length': len(socios_serial),
            'represents': represents,
            'contratantes_chart': json.dumps(contratantes_count_serial),
            'contratantes_length': len(contratantes_count_serial),
            'contratos': contratos,
            'suma_contratos': contratos.aggregate(sum=Sum('montoorigen', filter=Q(ruc=ruc))),
            'tipocontratos_chart': json.dumps(tipocontratos_count_serial),
        }

        return render(request, 'perfil.html', context)
    except ProveedoresBuscadorUtf.DoesNotExist:
        return redirect('main_page')
