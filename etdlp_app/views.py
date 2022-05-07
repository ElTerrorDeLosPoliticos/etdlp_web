from django.db.models import Count, Q, Sum
from django.shortcuts import render, redirect
from django.http import Http404
from legacy import models as legacy_models
from etdlp_app.serializers import SocioSerializer, AdministrativosSerializer, GeograficasSerializer, ContratoSerializer, ContratantesCountSerializer, TipoContratoCountSerializer, SancionesSerializer, PerfilSerializer, RankingContratosSerializer, RankingMontoSerializer, RankingSancionesSerializer
import json


# Create your views here.
def main_page(request):
    return render(request, 'index.html', {})


def perfil_empresa(request, ruc):
    try:
        empresa = legacy_models.ProveedoresBuscadorUtf.objects.get(ruc=ruc)
        context = {
            'empresa': empresa,
        }

        socios = legacy_models.ProveedoresPerfilSociosUtf.objects.filter(ruc=ruc)
        socios_serial = SocioSerializer(socios, many=True).data

        represents = legacy_models.ProveedoresPerfilRepresentantesUtf.objects.filter(ruc=ruc)

        administrativos = legacy_models.ProveedoresPerfilOrgAdministrativosCsv.objects.filter(ruc=ruc)
        administrativos_serial = AdministrativosSerializer(administrativos, many=True).data

        geograficas = legacy_models.ProveedoresPerfilInfoGeoUtf.objects.filter(numeroruc=ruc)
        geograficas_serial = GeograficasSerializer(geograficas, many=True).data

        context.update({
            'socios_length': len(socios_serial),
            'socios_chart': json.dumps(socios_serial),

            'represents': represents,

            'administrativos': json.dumps(administrativos_serial),

            'geograficas': json.dumps(geograficas_serial),
        })

        contratantes_count = legacy_models.ProveedoresPerfilSeaceUtf.objects.filter(ruc=ruc).values('nomentcont').annotate(total=Count('razon_social', filter=Q(ruc=ruc)))
        contratantes_count_serial = ContratantesCountSerializer(contratantes_count, many=True).data

        contratos = legacy_models.ProveedoresPerfilSeaceUtf.objects.filter(ruc=ruc)
        contratos_serial = ContratoSerializer(contratos, many=True).data

        tipocontratos_count = legacy_models.ProveedoresPerfilSeaceUtf.objects.values('descatobj2').annotate(value=Count('descatobj2', filter=Q(ruc=ruc))).order_by('descatobj2')
        tipocontratos_count_serial = TipoContratoCountSerializer(tipocontratos_count, many=True).data

        context.update({
            'suma_contratos': contratos.aggregate(sum=Sum('montoorigen', filter=Q(ruc=ruc))),

            'contratantes_chart': json.dumps(contratantes_count_serial),
            'contratantes_length': len(contratantes_count_serial),

            'tipocontratos_chart': json.dumps(tipocontratos_count_serial),

            'contratos_length': len(contratos_serial),
            'contratos': json.dumps(contratos_serial),
        })

        sanciones = legacy_models.ProveedoresPerfilSancionesUtf.objects.filter(numeroruc=ruc)
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
    except legacy_models.ProveedoresBuscadorUtf.DoesNotExist:
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
    return render(request, 'buscador/buscador_base.html', context)


def resultado_proveedores(request):
    query = request.GET.get('q', '')
    context = {
        **portada_proveedores,
        'query': query.strip(),
    }
    return render(request, 'resultados/resultados_proveedores.html', context)


portada_reportes = {
    'contratos': {
        'title': 'Contratos de Interés',
        'meaning': 'c',
        'html': 'contratos',
    },
    'empresas': {
        'title': 'Empresas de Interés',
        'meaning': 'e',
        'html': 'empresas_interes',
    },
    'sanciones': {
        'title': 'Sancionadas',
        'meaning': 's',
        'html': 'sanciones',
    },
}


# def buscador_reportes(request, tabla):
#     if tabla in ['empresas', 'contratos', 'sanciones']:
#         context = {
#             **portada_reportes,
#             'title': portada_reportes.get(tabla).get('title'),
#         }
#         return render(request, 'buscador/buscador_base.html', context)
#     else:
#         raise Http404()


def resultado_reportes(request, tabla):
    if tabla in ['empresas', 'contratos', 'sanciones']:
        query = request.GET.get('q', '')
        context = {
            'placeholder': 'RUC o Razón Social',
            'title': portada_reportes.get(tabla).get('title'),
            'meaning': portada_reportes.get(tabla).get('meaning'),
            'query': query.strip(),
        }
        if tabla == 'sanciones':
            r_monto = legacy_models.AnalysisEmpresasSancionadasContratadoras.objects.all().order_by('-monto_ganado')[:9]
            r_monto_serial = RankingMontoSerializer(r_monto, many=True).data

            r_sanciones = legacy_models.AnalysisEmpresasSancionadasContratadoras.objects.all().order_by('-sanciones')[:10]
            r_sanciones_serial = RankingSancionesSerializer(r_sanciones, many=True).data

            r_contratos = legacy_models.AnalysisEmpresasSancionadasContratadoras.objects.all().order_by('-contratos_ganados')[:8]
            r_contratos_serial = RankingContratosSerializer(r_contratos, many=True).data

            tipo_sanciones_chart = []
            for le in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
                tipo_sanciones_chart.append({
                    'name': le,
                    'value': legacy_models.AnalysisEmpresasSancionadasContratadoras.objects.aggregate(Sum(le.lower())).get('{}__sum'.format(le.lower()), 0.00)
                })

            reportes = {
                'ranking_monto': json.dumps(r_monto_serial),
                'ranking_monto_length': len(r_monto),
                'ranking_sanciones': json.dumps(r_sanciones_serial),
                'ranking_sanciones_length': len(r_sanciones),
                'ranking_contratos': json.dumps(r_contratos_serial),
                'ranking_contratos_length': len(r_contratos),
                'tipo_sanciones_chart': tipo_sanciones_chart,
            }
            context = {
                **context, **reportes
            }

        return render(request, 'resultados/resultados_{}.html'.format(portada_reportes.get(tabla).get('html')), context)
    else:
        raise Http404()


def buscador_perfiles(request):
    context = {
        'title': 'Buscador de Perfiles',
        'description': 'Busca según RUC',
        'img': 'project/img/img_perfiles.png',
        'placeholder': 'RUC',
    }
    return render(request, 'buscador/buscador_base.html', context)
