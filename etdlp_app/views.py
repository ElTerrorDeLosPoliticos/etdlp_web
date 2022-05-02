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
        context = {
            'empresa': empresa,
        }

        socios = ProveedoresPerfilSociosUtf.objects.filter(ruc=ruc)
        socios_serial = SocioSerializer(socios, many=True).data

        represents = ProveedoresPerfilRepresentantesUtf.objects.filter(ruc=ruc)

        administrativos = ProveedoresPerfilOrgAdministrativosCsv.objects.filter(ruc=ruc)
        administrativos_serial = AdministrativosSerializer(administrativos, many=True).data

        geograficas = ProveedoresPerfilInfoGeoUtf.objects.filter(numeroruc=ruc)
        geograficas_serial = GeograficasSerializer(geograficas, many=True).data

        context.update({
            'socios_length': len(socios_serial),
            'socios_chart': json.dumps(socios_serial),

            'represents': represents,

            'administrativos': json.dumps(administrativos_serial),

            'geograficas': json.dumps(geograficas_serial),
        })

        contratantes_count = ProveedoresPerfilSeaceUtf.objects.filter(ruc=ruc).values('nomentcont').annotate(total=Count('razon_social', filter=Q(ruc=ruc)))
        contratantes_count_serial = ContratantesCountSerializer(contratantes_count, many=True).data

        contratos = ProveedoresPerfilSeaceUtf.objects.filter(ruc=ruc)
        contratos_serial = ContratoSerializer(contratos, many=True).data

        tipocontratos_count = ProveedoresPerfilSeaceUtf.objects.values('descatobj2').annotate(value=Count('descatobj2', filter=Q(ruc=ruc))).order_by('descatobj2')
        tipocontratos_count_serial = TipoContratoCountSerializer(tipocontratos_count, many=True).data

        context.update({
            'suma_contratos': contratos.aggregate(sum=Sum('montoorigen', filter=Q(ruc=ruc))),

            'contratantes_chart': json.dumps(contratantes_count_serial),
            'contratantes_length': len(contratantes_count_serial),

            'tipocontratos_chart': json.dumps(tipocontratos_count_serial),

            'contratos_length': len(contratos_serial),
            'contratos': json.dumps(contratos_serial),
        })

        sanciones = ProveedoresPerfilSancionesUtf.objects.filter(numeroruc=ruc)
        sanciones_serial = SancionesSerializer(sanciones, many=True).data

        min_fecha = sanciones.order_by('fechaini_field').first().fechaini_field if sanciones else ''
        max_fecha = sanciones.order_by('-fechafin_field').first().fechafin_field if sanciones else ''
        vigentes = sanciones.filter(vigente=True).count()

        context.update({
            'sanciones': json.dumps(sanciones_serial),
            'sanciones_length': len(sanciones_serial),
            'vigentes': vigentes,
            'min_fecha_sanciones': min_fecha[:4],
            'max_fecha_sanciones': max_fecha[:4],
        })
        return render(request, 'perfil.html', context)
    except ProveedoresBuscadorUtf.DoesNotExist:
        return redirect('buscador_perfiles')


portada_proveedores = {
    'title': 'Buscador de Proveedores',
    'description': 'Contiene información de los proveedores que han adjudicado procedimientos. El proveedor puede ser individual (persona natural o jurídica) o un consorcio. ',
    'img': 'project/img/img_proveedores.png',
    'placeholder': 'DNI, RUC o Nombre',
    'url_resultado': 'resultado_proveedores',
}


def buscador_proveedores(request):
    context = {
        **portada_proveedores
    }
    return render(request, 'buscador.html', context)


def resultado_proveedores(request):
    query = request.GET.get('q', '')
    context = {
        **portada_proveedores,
        'query': query.strip(),
    }
    return render(request, 'resultados.html', context)


def buscador_perfiles(request):
    context = {
        'title': 'Buscador de Perfiles',
        'description': 'Busca según RUC',
        'img': 'project/img/img_perfiles.png',
        'placeholder': 'RUC',
    }
    return render(request, 'buscador.html', context)
