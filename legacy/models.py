# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProductoPlanillaBuscadorCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    registro = models.BigIntegerField(blank=True, null=True)
    vc_personal_nombres = models.TextField(db_column='VC_PERSONAL_NOMBRES', blank=True, null=True)  # Field name made lowercase.
    vc_personal_paterno = models.TextField(db_column='VC_PERSONAL_PATERNO', blank=True, null=True)  # Field name made lowercase.
    vc_personal_materno = models.TextField(db_column='VC_PERSONAL_MATERNO', blank=True, null=True)  # Field name made lowercase.
    entidad = models.TextField(db_column='ENTIDAD', blank=True, null=True)  # Field name made lowercase.
    vc_personal_dependencia = models.TextField(db_column='VC_PERSONAL_DEPENDENCIA', blank=True, null=True)  # Field name made lowercase.
    vc_personal_regimen_laboral = models.BigIntegerField(db_column='VC_PERSONAL_REGIMEN_LABORAL', blank=True, null=True)  # Field name made lowercase.
    vc_personal_cargo = models.TextField(db_column='VC_PERSONAL_CARGO', blank=True, null=True)  # Field name made lowercase.
    vc_personal_ruc_entidad = models.BigIntegerField(db_column='VC_PERSONAL_RUC_ENTIDAD', blank=True, null=True)  # Field name made lowercase.
    pk_id_personal = models.BigIntegerField(db_column='PK_ID_PERSONAL', blank=True, null=True)  # Field name made lowercase.
    fec_reg = models.TextField(db_column='FEC_REG', blank=True, null=True)  # Field name made lowercase.
    in_personal_anno = models.BigIntegerField(db_column='IN_PERSONAL_ANNO', blank=True, null=True)  # Field name made lowercase.
    in_personal_mes = models.BigIntegerField(db_column='IN_PERSONAL_MES', blank=True, null=True)  # Field name made lowercase.
    mo_personal_total = models.FloatField(db_column='MO_PERSONAL_TOTAL', blank=True, null=True)  # Field name made lowercase.
    mo_personal_honorarios = models.FloatField(db_column='MO_PERSONAL_HONORARIOS', blank=True, null=True)  # Field name made lowercase.
    mo_personal_remuneraciones = models.FloatField(db_column='MO_PERSONAL_REMUNERACIONES', blank=True, null=True)  # Field name made lowercase.
    mo_personal_gratificacion = models.FloatField(db_column='MO_PERSONAL_GRATIFICACION', blank=True, null=True)  # Field name made lowercase.
    mo_personal_incentivo = models.FloatField(db_column='MO_PERSONAL_INCENTIVO', blank=True, null=True)  # Field name made lowercase.
    mo_personal_otros_beneficios = models.FloatField(db_column='MO_PERSONAL_OTROS_BENEFICIOS', blank=True, null=True)  # Field name made lowercase.
    vc_personal_observaciones = models.TextField(db_column='VC_PERSONAL_OBSERVACIONES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_planilla_buscador.csv'


class ProductoPlanillaBuscadorUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registro = models.BigIntegerField(blank=True, null=True)
    vc_personal_nombres = models.TextField(db_column='VC_PERSONAL_NOMBRES', blank=True, null=True)  # Field name made lowercase.
    vc_personal_paterno = models.TextField(db_column='VC_PERSONAL_PATERNO', blank=True, null=True)  # Field name made lowercase.
    vc_personal_materno = models.TextField(db_column='VC_PERSONAL_MATERNO', blank=True, null=True)  # Field name made lowercase.
    entidad = models.TextField(db_column='ENTIDAD', blank=True, null=True)  # Field name made lowercase.
    vc_personal_dependencia = models.TextField(db_column='VC_PERSONAL_DEPENDENCIA', blank=True, null=True)  # Field name made lowercase.
    vc_personal_regimen_laboral = models.BigIntegerField(db_column='VC_PERSONAL_REGIMEN_LABORAL', blank=True, null=True)  # Field name made lowercase.
    vc_personal_cargo = models.TextField(db_column='VC_PERSONAL_CARGO', blank=True, null=True)  # Field name made lowercase.
    vc_personal_ruc_entidad = models.BigIntegerField(db_column='VC_PERSONAL_RUC_ENTIDAD', blank=True, null=True)  # Field name made lowercase.
    pk_id_personal = models.BigIntegerField(db_column='PK_ID_PERSONAL', blank=True, null=True)  # Field name made lowercase.
    fec_reg = models.TextField(db_column='FEC_REG', blank=True, null=True)  # Field name made lowercase.
    in_personal_anno = models.BigIntegerField(db_column='IN_PERSONAL_ANNO', blank=True, null=True)  # Field name made lowercase.
    in_personal_mes = models.BigIntegerField(db_column='IN_PERSONAL_MES', blank=True, null=True)  # Field name made lowercase.
    mo_personal_total = models.FloatField(db_column='MO_PERSONAL_TOTAL', blank=True, null=True)  # Field name made lowercase.
    mo_personal_honorarios = models.FloatField(db_column='MO_PERSONAL_HONORARIOS', blank=True, null=True)  # Field name made lowercase.
    mo_personal_remuneraciones = models.FloatField(db_column='MO_PERSONAL_REMUNERACIONES', blank=True, null=True)  # Field name made lowercase.
    mo_personal_gratificacion = models.FloatField(db_column='MO_PERSONAL_GRATIFICACION', blank=True, null=True)  # Field name made lowercase.
    mo_personal_incentivo = models.FloatField(db_column='MO_PERSONAL_INCENTIVO', blank=True, null=True)  # Field name made lowercase.
    mo_personal_otros_beneficios = models.FloatField(db_column='MO_PERSONAL_OTROS_BENEFICIOS', blank=True, null=True)  # Field name made lowercase.
    vc_personal_observaciones = models.TextField(db_column='VC_PERSONAL_OBSERVACIONES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_planilla_buscador_utf'


class ProductoPlanillaPerfilCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    id = models.BigIntegerField(blank=True, null=True)
    nombre_completo = models.TextField(db_column='nombre completo', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    salario_mensual_promedio_s_field = models.FloatField(db_column='salario mensual promedio (S/.)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    meses_trabajados = models.BigIntegerField(db_column='meses trabajados', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primer_mes = models.BigIntegerField(db_column='primer mes', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ultimo_mes = models.BigIntegerField(db_column='ultimo mes', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_cargos = models.BigIntegerField(db_column='n cargos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cargo = models.TextField(blank=True, null=True)
    ndependencias = models.BigIntegerField(blank=True, null=True)
    dependencias = models.TextField(blank=True, null=True)
    salario_promedio_s_field = models.TextField(db_column='salario promedio (S/.)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salario_std = models.TextField(db_column='salario std', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number_3s_outlier = models.BigIntegerField(db_column='3s_outlier', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_6s_outlier = models.BigIntegerField(db_column='6s_outlier', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'producto_planilla_perfil.csv'


class ProductoPlanillaPerfilUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.BigIntegerField(blank=True, null=True)
    nombre_completo = models.TextField(db_column='nombre completo', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    salario_mensual_promedio_s_field = models.FloatField(db_column='salario mensual promedio (S/.)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    meses_trabajados = models.BigIntegerField(db_column='meses trabajados', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primer_mes = models.BigIntegerField(db_column='primer mes', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ultimo_mes = models.BigIntegerField(db_column='ultimo mes', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    n_cargos = models.BigIntegerField(db_column='n cargos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cargo = models.TextField(blank=True, null=True)
    ndependencias = models.BigIntegerField(blank=True, null=True)
    dependencias = models.TextField(blank=True, null=True)
    salario_promedio_s_field = models.TextField(db_column='salario promedio (S/.)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salario_std = models.TextField(db_column='salario std', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number_3s_outlier = models.BigIntegerField(db_column='3s_outlier', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_6s_outlier = models.BigIntegerField(db_column='6s_outlier', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'producto_planilla_perfil_utf'


class ProductoProveedoresBuscadorCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    id = models.BigIntegerField(blank=True, null=True)
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    tipoempresa = models.TextField(db_column='tipoEmpresa', blank=True, null=True)  # Field name made lowercase.
    seace_registros = models.FloatField(blank=True, null=True)
    seace_gasto_total = models.FloatField(blank=True, null=True)
    seace_gasto_promedio_mensual = models.FloatField(blank=True, null=True)
    seace_fecha_min = models.TextField(blank=True, null=True)
    seace_fecha_max = models.TextField(blank=True, null=True)
    n_sanciones = models.FloatField(blank=True, null=True)
    meses_sancionado = models.FloatField(blank=True, null=True)
    organos_nomb_apell = models.TextField(blank=True, null=True)
    organos_nrodocumento = models.TextField(db_column='organos_nroDocumento', blank=True, null=True)  # Field name made lowercase.
    representantes_nomb_apell = models.TextField(blank=True, null=True)
    representantes_nrodocumento = models.TextField(db_column='representantes_nroDocumento', blank=True, null=True)  # Field name made lowercase.
    socios = models.TextField(blank=True, null=True)
    socios_dni = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_proveedores_buscador.csv'


class ProductoProveedoresBuscadorUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.BigIntegerField(blank=True, null=True)
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    tipoempresa = models.TextField(db_column='tipoEmpresa', blank=True, null=True)  # Field name made lowercase.
    seace_registros = models.FloatField(blank=True, null=True)
    seace_gasto_total = models.FloatField(blank=True, null=True)
    seace_gasto_promedio_mensual = models.FloatField(blank=True, null=True)
    seace_fecha_min = models.TextField(blank=True, null=True)
    seace_fecha_max = models.TextField(blank=True, null=True)
    n_sanciones = models.FloatField(blank=True, null=True)
    meses_sancionado = models.FloatField(blank=True, null=True)
    organos_nomb_apell = models.TextField(blank=True, null=True)
    organos_nrodocumento = models.TextField(db_column='organos_nroDocumento', blank=True, null=True)  # Field name made lowercase.
    representantes_nomb_apell = models.TextField(blank=True, null=True)
    representantes_nrodocumento = models.TextField(db_column='representantes_nroDocumento', blank=True, null=True)  # Field name made lowercase.
    socios = models.TextField(blank=True, null=True)
    socios_dni = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_proveedores_buscador_utf'


class ProductoProveedoresPerfilInfoGeoCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numeroruc = models.BigIntegerField(db_column='numeroRuc', blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.TextField(db_column='razonSocial', blank=True, null=True)  # Field name made lowercase.
    tipoempresa = models.TextField(db_column='tipoEmpresa', blank=True, null=True)  # Field name made lowercase.
    departamento = models.TextField(blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    provincia = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    condicion = models.TextField(blank=True, null=True)
    codigoregistro = models.TextField(db_column='codigoRegistro', blank=True, null=True)  # Field name made lowercase.
    clctexto = models.TextField(db_column='clcTexto', blank=True, null=True)  # Field name made lowercase.
    cmctexto = models.TextField(db_column='cmcTexto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_info_geo.csv'


class ProductoProveedoresPerfilInfoGeoUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0_1 = models.BigIntegerField(db_column='Unnamed: 0.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numeroruc = models.BigIntegerField(db_column='numeroRuc', blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.TextField(db_column='razonSocial', blank=True, null=True)  # Field name made lowercase.
    tipoempresa = models.TextField(db_column='tipoEmpresa', blank=True, null=True)  # Field name made lowercase.
    departamento = models.TextField(blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    provincia = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    condicion = models.TextField(blank=True, null=True)
    codigoregistro = models.TextField(db_column='codigoRegistro', blank=True, null=True)  # Field name made lowercase.
    clctexto = models.TextField(db_column='clcTexto', blank=True, null=True)  # Field name made lowercase.
    cmctexto = models.TextField(db_column='cmcTexto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_info_geo_utf'


class ProductoProveedoresPerfilOrgAdministrativosCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    apellidosnomb = models.TextField(db_column='apellidosNomb', blank=True, null=True)  # Field name made lowercase.
    sigladocide = models.TextField(db_column='siglaDocIde', blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.BigIntegerField(db_column='nroDocumento', blank=True, null=True)  # Field name made lowercase.
    desccargo = models.TextField(db_column='descCargo', blank=True, null=True)  # Field name made lowercase.
    desctipoorgano = models.TextField(db_column='descTipoOrgano', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.TextField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_org_administrativos.csv'


class ProductoProveedoresPerfilRepresentantesCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    apellidosnomb = models.TextField(db_column='apellidosNomb', blank=True, null=True)  # Field name made lowercase.
    sigladocide = models.TextField(db_column='siglaDocIde', blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.BigIntegerField(db_column='nroDocumento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_representantes.csv'


class ProductoProveedoresPerfilRepresentantesUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0_1 = models.BigIntegerField(db_column='Unnamed: 0.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    apellidosnomb = models.TextField(db_column='apellidosNomb', blank=True, null=True)  # Field name made lowercase.
    sigladocide = models.TextField(db_column='siglaDocIde', blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.BigIntegerField(db_column='nroDocumento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_representantes_utf'


class ProductoProveedoresPerfilSancionesCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numeroruc = models.BigIntegerField(db_column='numeroRuc', blank=True, null=True)  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(blank=True, null=True)
    idscausales = models.BigIntegerField(db_column='idsCausales', blank=True, null=True)  # Field name made lowercase.
    motivos = models.TextField(blank=True, null=True)
    fechaini_field = models.TextField(db_column='fechaIni_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    fechafin_field = models.TextField(db_column='fechaFin_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    meses_sancionado = models.BigIntegerField(blank=True, null=True)
    vigente = models.BooleanField(blank=True, null=True)
    montotexto = models.FloatField(db_column='montoTexto', blank=True, null=True)  # Field name made lowercase.
    nrores = models.TextField(db_column='nroRes', blank=True, null=True)  # Field name made lowercase.
    fecharesol = models.TextField(db_column='fechaResol', blank=True, null=True)  # Field name made lowercase.
    idnuminhab = models.BigIntegerField(db_column='idNumInhab', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_sanciones.csv'


class ProductoProveedoresPerfilSancionesUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0_1 = models.BigIntegerField(db_column='Unnamed: 0.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numeroruc = models.BigIntegerField(db_column='numeroRuc', blank=True, null=True)  # Field name made lowercase.
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(blank=True, null=True)
    idscausales = models.BigIntegerField(db_column='idsCausales', blank=True, null=True)  # Field name made lowercase.
    motivos = models.TextField(blank=True, null=True)
    fechaini_field = models.TextField(db_column='fechaIni_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    fechafin_field = models.TextField(db_column='fechaFin_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    meses_sancionado = models.BigIntegerField(blank=True, null=True)
    vigente = models.BooleanField(blank=True, null=True)
    montotexto = models.FloatField(db_column='montoTexto', blank=True, null=True)  # Field name made lowercase.
    nrores = models.TextField(db_column='nroRes', blank=True, null=True)  # Field name made lowercase.
    fecharesol = models.TextField(db_column='fechaResol', blank=True, null=True)  # Field name made lowercase.
    idnuminhab = models.BigIntegerField(db_column='idNumInhab', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_sanciones_utf'


class ProductoProveedoresPerfilSeaceCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha = models.TextField(blank=True, null=True)
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    nomentcont = models.TextField(db_column='nomEntCont', blank=True, null=True)  # Field name made lowercase.
    descontprov = models.TextField(db_column='desContProv', blank=True, null=True)  # Field name made lowercase.
    montoorigen = models.FloatField(db_column='montoOrigen', blank=True, null=True)  # Field name made lowercase.
    desestcontprov = models.TextField(db_column='desEstContProv', blank=True, null=True)  # Field name made lowercase.
    descatobj2 = models.TextField(db_column='desCatObj2', blank=True, null=True)  # Field name made lowercase.
    codcontprov = models.TextField(db_column='codContProv', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_seace.csv'


class ProductoProveedoresPerfilSeaceUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0_1 = models.BigIntegerField(db_column='Unnamed: 0.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha = models.TextField(blank=True, null=True)
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    nomentcont = models.TextField(db_column='nomEntCont', blank=True, null=True)  # Field name made lowercase.
    descontprov = models.TextField(db_column='desContProv', blank=True, null=True)  # Field name made lowercase.
    montoorigen = models.FloatField(db_column='montoOrigen', blank=True, null=True)  # Field name made lowercase.
    desestcontprov = models.TextField(db_column='desEstContProv', blank=True, null=True)  # Field name made lowercase.
    descatobj2 = models.TextField(db_column='desCatObj2', blank=True, null=True)  # Field name made lowercase.
    codcontprov = models.TextField(db_column='codContProv', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_seace_utf'


class ProductoProveedoresPerfilSociosCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.TextField(db_column='razonSocial', blank=True, null=True)  # Field name made lowercase.
    sigladocide = models.TextField(db_column='siglaDocIde', blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.BigIntegerField(db_column='nroDocumento', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.TextField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    porcentajeacciones = models.FloatField(db_column='porcentajeAcciones', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_socios.csv'


class ProductoProveedoresPerfilSociosUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0_1 = models.BigIntegerField(db_column='Unnamed: 0.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.TextField(db_column='razonSocial', blank=True, null=True)  # Field name made lowercase.
    sigladocide = models.TextField(db_column='siglaDocIde', blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.BigIntegerField(db_column='nroDocumento', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.TextField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    porcentajeacciones = models.FloatField(db_column='porcentajeAcciones', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_proveedores_perfil_socios_utf'


class ProductoVisitantesBuscadorCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha = models.TextField(blank=True, null=True)
    hora_ingreso = models.TextField(db_column='Hora_Ingreso', blank=True, null=True)  # Field name made lowercase.
    hora_salida = models.TextField(db_column='Hora_Salida', blank=True, null=True)  # Field name made lowercase.
    motivo = models.TextField(db_column='Motivo', blank=True, null=True)  # Field name made lowercase.
    visitante = models.TextField(db_column='Visitante', blank=True, null=True)  # Field name made lowercase.
    tipo_documento = models.TextField(db_column='Tipo_Documento', blank=True, null=True)  # Field name made lowercase.
    n_documento = models.TextField(db_column='N_Documento', blank=True, null=True)  # Field name made lowercase.
    institucion = models.TextField(db_column='Institucion', blank=True, null=True)  # Field name made lowercase.
    visitado = models.TextField(db_column='Visitado', blank=True, null=True)  # Field name made lowercase.
    entidad = models.TextField(blank=True, null=True)
    cargo = models.TextField(db_column='Cargo', blank=True, null=True)  # Field name made lowercase.
    oficina = models.TextField(db_column='Oficina', blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_visitantes_buscador.csv'


class ProductoVisitantesBuscadorUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0_1 = models.BigIntegerField(db_column='Unnamed: 0.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha = models.TextField(blank=True, null=True)
    hora_ingreso = models.TextField(db_column='Hora_Ingreso', blank=True, null=True)  # Field name made lowercase.
    hora_salida = models.TextField(db_column='Hora_Salida', blank=True, null=True)  # Field name made lowercase.
    motivo = models.TextField(db_column='Motivo', blank=True, null=True)  # Field name made lowercase.
    visitante = models.TextField(db_column='Visitante', blank=True, null=True)  # Field name made lowercase.
    tipo_documento = models.TextField(db_column='Tipo_Documento', blank=True, null=True)  # Field name made lowercase.
    n_documento = models.TextField(db_column='N_Documento', blank=True, null=True)  # Field name made lowercase.
    institucion = models.TextField(db_column='Institucion', blank=True, null=True)  # Field name made lowercase.
    visitado = models.TextField(db_column='Visitado', blank=True, null=True)  # Field name made lowercase.
    entidad = models.TextField(blank=True, null=True)
    cargo = models.TextField(db_column='Cargo', blank=True, null=True)  # Field name made lowercase.
    oficina = models.TextField(db_column='Oficina', blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_visitantes_buscador_utf'


class ProductoVisitantesEmpresariosCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seace_registros = models.FloatField(blank=True, null=True)
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    tipoempresa = models.TextField(db_column='tipoEmpresa', blank=True, null=True)  # Field name made lowercase.
    seace_gasto_promedio_mensual = models.FloatField(blank=True, null=True)
    seace_fecha_min = models.TextField(blank=True, null=True)
    seace_fecha_max = models.TextField(blank=True, null=True)
    ganados_despues_visita = models.BigIntegerField(blank=True, null=True)
    monto_promedio_despues_visita = models.FloatField(blank=True, null=True)
    n_sanciones = models.FloatField(blank=True, null=True)
    meses_sancionado = models.FloatField(blank=True, null=True)
    visitante = models.TextField(db_column='Visitante', blank=True, null=True)  # Field name made lowercase.
    tipo_documento = models.TextField(db_column='Tipo_Documento', blank=True, null=True)  # Field name made lowercase.
    n_documento_field = models.BigIntegerField(db_column='N_Documento_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    es_organo = models.BigIntegerField(blank=True, null=True)
    es_representante = models.BigIntegerField(blank=True, null=True)
    es_socio = models.BigIntegerField(blank=True, null=True)
    es_persona_natural = models.BigIntegerField(blank=True, null=True)
    fechas = models.BigIntegerField(blank=True, null=True)
    field_visitas = models.BigIntegerField(db_column='#_Visitas', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    tiempo_reuniones_min_field = models.FloatField(db_column='Tiempo_reuniones(min)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    primer_dia = models.TextField(blank=True, null=True)
    ultimo_dia = models.TextField(blank=True, null=True)
    reunion_sin_tiempo = models.BigIntegerField(blank=True, null=True)
    field_visitados = models.BigIntegerField(db_column='#_Visitados', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    visitados = models.TextField(db_column='Visitados', blank=True, null=True)  # Field name made lowercase.
    cargos = models.TextField(db_column='Cargos', blank=True, null=True)  # Field name made lowercase.
    field_oficinas = models.BigIntegerField(db_column='#_oficinas', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    oficinas = models.TextField(db_column='Oficinas', blank=True, null=True)  # Field name made lowercase.
    entidades = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_visitantes_empresarios.csv'


class ProductoVisitantesEmpresariosUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0_1 = models.BigIntegerField(db_column='Unnamed: 0.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seace_registros = models.FloatField(blank=True, null=True)
    ruc = models.BigIntegerField(blank=True, null=True)
    razon_social = models.TextField(db_column='Razon_social', blank=True, null=True)  # Field name made lowercase.
    tipoempresa = models.TextField(db_column='tipoEmpresa', blank=True, null=True)  # Field name made lowercase.
    seace_gasto_promedio_mensual = models.FloatField(blank=True, null=True)
    seace_fecha_min = models.TextField(blank=True, null=True)
    seace_fecha_max = models.TextField(blank=True, null=True)
    ganados_despues_visita = models.BigIntegerField(blank=True, null=True)
    monto_promedio_despues_visita = models.FloatField(blank=True, null=True)
    n_sanciones = models.FloatField(blank=True, null=True)
    meses_sancionado = models.FloatField(blank=True, null=True)
    visitante = models.TextField(db_column='Visitante', blank=True, null=True)  # Field name made lowercase.
    tipo_documento = models.TextField(db_column='Tipo_Documento', blank=True, null=True)  # Field name made lowercase.
    n_documento_field = models.BigIntegerField(db_column='N_Documento_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    es_organo = models.BigIntegerField(blank=True, null=True)
    es_representante = models.BigIntegerField(blank=True, null=True)
    es_socio = models.BigIntegerField(blank=True, null=True)
    es_persona_natural = models.BigIntegerField(blank=True, null=True)
    fechas = models.BigIntegerField(blank=True, null=True)
    field_visitas = models.BigIntegerField(db_column='#_Visitas', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    tiempo_reuniones_min_field = models.FloatField(db_column='Tiempo_reuniones(min)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    primer_dia = models.TextField(blank=True, null=True)
    ultimo_dia = models.TextField(blank=True, null=True)
    reunion_sin_tiempo = models.BigIntegerField(blank=True, null=True)
    field_visitados = models.BigIntegerField(db_column='#_Visitados', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    visitados = models.TextField(db_column='Visitados', blank=True, null=True)  # Field name made lowercase.
    cargos = models.TextField(db_column='Cargos', blank=True, null=True)  # Field name made lowercase.
    field_oficinas = models.BigIntegerField(db_column='#_oficinas', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    oficinas = models.TextField(db_column='Oficinas', blank=True, null=True)  # Field name made lowercase.
    entidades = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_visitantes_empresarios_utf'


class ProductoVisitantesPerfilCsv(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.BigIntegerField(blank=True, null=True)
    visitante = models.TextField(db_column='Visitante', blank=True, null=True)  # Field name made lowercase.
    fechas = models.BigIntegerField(blank=True, null=True)
    field_visitas = models.BigIntegerField(db_column='#_Visitas', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    tiempo_reuniones_min_field = models.FloatField(db_column='Tiempo_reuniones(min)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tiempo_reunion_n_fechas_h_field = models.FloatField(db_column='tiempo_reunion/n_fechas (h)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    primer_dia = models.TextField(blank=True, null=True)
    ultimo_dia = models.TextField(blank=True, null=True)
    reunion_sin_tiempo = models.BigIntegerField(blank=True, null=True)
    field_visitados = models.BigIntegerField(db_column='#_Visitados', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    visitados = models.TextField(db_column='Visitados', blank=True, null=True)  # Field name made lowercase.
    tipo_documento = models.TextField(db_column='Tipo_Documento', blank=True, null=True)  # Field name made lowercase.
    n_documento = models.TextField(db_column='N_Documento', blank=True, null=True)  # Field name made lowercase.
    cargos = models.TextField(db_column='Cargos', blank=True, null=True)  # Field name made lowercase.
    field_oficinas = models.BigIntegerField(db_column='#_oficinas', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    oficinas = models.TextField(db_column='Oficinas', blank=True, null=True)  # Field name made lowercase.
    entidades = models.TextField(blank=True, null=True)
    n_entidades = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_visitantes_perfil.csv'


class ProductoVisitantesPerfilUtf(models.Model):
    index = models.BigIntegerField(primary_key=True)
    unnamed_0_1 = models.BigIntegerField(db_column='Unnamed: 0.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.BigIntegerField(blank=True, null=True)
    visitante = models.TextField(db_column='Visitante', blank=True, null=True)  # Field name made lowercase.
    fechas = models.BigIntegerField(blank=True, null=True)
    field_visitas = models.BigIntegerField(db_column='#_Visitas', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    tiempo_reuniones_min_field = models.FloatField(db_column='Tiempo_reuniones(min)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tiempo_reunion_n_fechas_h_field = models.FloatField(db_column='tiempo_reunion/n_fechas (h)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    primer_dia = models.TextField(blank=True, null=True)
    ultimo_dia = models.TextField(blank=True, null=True)
    reunion_sin_tiempo = models.BigIntegerField(blank=True, null=True)
    field_visitados = models.BigIntegerField(db_column='#_Visitados', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    visitados = models.TextField(db_column='Visitados', blank=True, null=True)  # Field name made lowercase.
    tipo_documento = models.TextField(db_column='Tipo_Documento', blank=True, null=True)  # Field name made lowercase.
    n_documento = models.TextField(db_column='N_Documento', blank=True, null=True)  # Field name made lowercase.
    cargos = models.TextField(db_column='Cargos', blank=True, null=True)  # Field name made lowercase.
    field_oficinas = models.BigIntegerField(db_column='#_oficinas', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    oficinas = models.TextField(db_column='Oficinas', blank=True, null=True)  # Field name made lowercase.
    entidades = models.TextField(blank=True, null=True)
    n_entidades = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_visitantes_perfil_utf'
