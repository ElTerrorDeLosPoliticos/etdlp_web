from django.shortcuts import render, redirect
from legacy.models import *


# Create your views here.
def main_page(request):
    return render(request, 'index.html', {})


def perfil_empresa(request, ruc):
    try:
        empresa = ProductoProveedoresBuscadorUtf.objects.get(ruc=ruc)
        return render(request, 'perfil.html', {'empresa': empresa})
    except ProductoProveedoresBuscadorUtf.DoesNotExist:
        return redirect('main_page')

