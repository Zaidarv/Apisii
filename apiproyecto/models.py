from django.db import models


class Alumnos(models.Model):
    no_de_control = models.CharField(primary_key=True, max_length=10)
    carrera = models.ForeignKey('Carreras', models.DO_NOTHING, db_column='carrera', blank=True, null=True)
    reticula = models.IntegerField(blank=True, null=True)
    especialidad = models.CharField(max_length=5, blank=True, null=True)
    nivel_escolar = models.CharField(max_length=1, blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)
    clave_interna = models.CharField(max_length=10, blank=True, null=True)
    estatus_alumno = models.CharField(max_length=3, blank=True, null=True)
    plan_de_estudios = models.CharField(max_length=1)
    apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    nombre_alumno = models.CharField(max_length=35, blank=True, null=True)
    curp_alumno = models.CharField(max_length=18)
    fecha_nacimiento = models.DateTimeField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    estado_civil = models.CharField(max_length=1, blank=True, null=True)
    tipo_ingreso = models.DecimalField(max_digits=1, decimal_places=0)
    periodo_ingreso_it = models.CharField(max_length=5)
    ultimo_periodo_inscrito = models.CharField(max_length=5, blank=True, null=True)
    promedio_periodo_anterior = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    promedio_aritmetico_acumulado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    creditos_aprobados = models.IntegerField(blank=True, null=True)
    creditos_cursados = models.IntegerField(blank=True, null=True)
    promedio_final_alcanzado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tipo_servicio_medico = models.CharField(max_length=10, blank=True, null=True)
    clave_servicio_medico = models.CharField(max_length=20, blank=True, null=True)
    escuela_procedencia = models.CharField(max_length=100, blank=True, null=True)
    tipo_escuela = models.IntegerField(blank=True, null=True)
    domicilio_escuela = models.CharField(max_length=60, blank=True, null=True)
    entidad_procedencia = models.IntegerField(blank=True, null=True)
    ciudad_procedencia = models.CharField(max_length=30, blank=True, null=True)
    correo_electronico = models.CharField(max_length=120, blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    firma = models.BinaryField(blank=True, null=True)
    periodos_revalidacion = models.IntegerField(blank=True, null=True)
    indice_reprobacion_acumulado = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    becado_por = models.CharField(max_length=100, blank=True, null=True)
    nip = models.IntegerField(blank=True, null=True)
    tipo_alumno = models.CharField(max_length=2, blank=True, null=True)
    nacionalidad = models.CharField(max_length=10, blank=True, null=True)
    usuario = models.CharField(max_length=30, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    folio = models.IntegerField(blank=True, null=True)
    horario_curso_java = models.CharField(max_length=50, blank=True, null=True)
    pago_curso_java = models.CharField(max_length=2, blank=True, null=True)
    periodo_estatus = models.CharField(max_length=5, blank=True, null=True)
    fecha_titulo = models.DateTimeField(blank=True, null=True)
    op_titula = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    libro = models.IntegerField(blank=True, null=True)
    hoja = models.IntegerField(blank=True, null=True)
    ultimo_login = models.DateTimeField(blank=True, null=True)
    id_sesion = models.CharField(max_length=100, blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    autoriza_padres = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumnos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Carreras(models.Model):
    carrera = models.CharField(primary_key=True, max_length=3)
    reticula = models.IntegerField()
    nivel_escolar = models.CharField(max_length=1)
    clave_oficial = models.CharField(max_length=20)
    nombre_carrera = models.CharField(max_length=80)
    nombre_reducido = models.CharField(max_length=30)
    siglas = models.CharField(max_length=10)
    carga_maxima = models.IntegerField()
    carga_minima = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(blank=True, null=True)
    clave_cosnet = models.CharField(max_length=2, blank=True, null=True)
    creditos_totales = models.IntegerField(blank=True, null=True)
    fichas = models.IntegerField(blank=True, null=True)
    modalidad = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carreras'
        unique_together = (('carrera', 'reticula'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PeriodosEscolares(models.Model):
    periodo = models.CharField(primary_key=True, max_length=5)
    identificacion_larga = models.CharField(max_length=30)
    identificacion_corta = models.CharField(max_length=12, blank=True, null=True)
    status = models.CharField(max_length=1)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    inicio_vacacional_ss = models.DateTimeField(blank=True, null=True)
    termino_vacacional_ss = models.DateTimeField(blank=True, null=True)
    num_dias_clase = models.IntegerField(blank=True, null=True)
    inicio_especial = models.DateTimeField(blank=True, null=True)
    fin_especial = models.DateTimeField(blank=True, null=True)
    cierre_horarios = models.CharField(max_length=1, blank=True, null=True)
    cierre_seleccion = models.CharField(max_length=1, blank=True, null=True)
    inicio_enc_estudiantil = models.DateTimeField(blank=True, null=True)
    fin_enc_estudiantil = models.DateTimeField(blank=True, null=True)
    inicio_sele_alumnos = models.DateTimeField(blank=True, null=True)
    fin_sele_alumnos = models.DateTimeField(blank=True, null=True)
    inicio_vacacional = models.DateTimeField(blank=True, null=True)
    termino_vacacional = models.DateTimeField(blank=True, null=True)
    parcial1_inicio = models.DateTimeField(blank=True, null=True)
    parcial1_fin = models.DateTimeField(blank=True, null=True)
    parcial2_inicio = models.DateTimeField(blank=True, null=True)
    parcial2_fin = models.DateTimeField(blank=True, null=True)
    parcial3_inicio = models.DateTimeField(blank=True, null=True)
    parcial3_fin = models.DateTimeField(blank=True, null=True)
    filtro = models.CharField(max_length=1, blank=True, null=True)
    nota = models.CharField(max_length=255, blank=True, null=True)
    inicio_captura_calificaciones = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodos_escolares'


class Personal(models.Model):
    rfc = models.CharField(primary_key=True, max_length=13)
    clave_centro_seit = models.CharField(max_length=10, blank=True, null=True)
    clave_area = models.CharField(max_length=6, blank=True, null=True)
    curp_empleado = models.CharField(max_length=18, blank=True, null=True)
    no_tarjeta = models.IntegerField(blank=True, null=True)
    apellidos_empleado = models.CharField(max_length=50, blank=True, null=True)
    nombre_empleado = models.CharField(max_length=35, blank=True, null=True)
    horas_nombramiento = models.IntegerField(blank=True, null=True)
    nombramiento = models.CharField(max_length=1)
    clases = models.CharField(max_length=1, blank=True, null=True)
    ingreso_rama = models.CharField(max_length=6, blank=True, null=True)
    inicio_gobierno = models.CharField(max_length=6, blank=True, null=True)
    inicio_sep = models.CharField(max_length=6, blank=True, null=True)
    inicio_plantel = models.CharField(max_length=6, blank=True, null=True)
    domicilio_empleado = models.CharField(max_length=60, blank=True, null=True)
    colonia_empleado = models.CharField(max_length=40, blank=True, null=True)
    codigo_postal_empleado = models.IntegerField(blank=True, null=True)
    localidad = models.CharField(max_length=30, blank=True, null=True)
    telefono_empleado = models.CharField(max_length=30, blank=True, null=True)
    sexo_empleado = models.CharField(max_length=1, blank=True, null=True)
    estado_civil = models.CharField(max_length=1, blank=True, null=True)
    fecha_nacimiento = models.DateTimeField(blank=True, null=True)
    lugar_nacimiento = models.IntegerField(blank=True, null=True)
    institucion_egreso = models.CharField(max_length=50, blank=True, null=True)
    nivel_estudios = models.CharField(max_length=1, blank=True, null=True)
    grado_maximo_estudios = models.CharField(max_length=1, blank=True, null=True)
    estudios = models.CharField(max_length=255, blank=True, null=True)
    fecha_termino_estudios = models.DateTimeField(blank=True, null=True)
    fecha_titulacion = models.DateTimeField(blank=True, null=True)
    cedula_profesional = models.CharField(max_length=15, blank=True, null=True)
    especializacion = models.CharField(max_length=50, blank=True, null=True)
    idiomas_domina = models.CharField(max_length=60, blank=True, null=True)
    status_empleado = models.CharField(max_length=2, blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    firma = models.BinaryField(blank=True, null=True)
    correo_electronico = models.CharField(max_length=150, blank=True, null=True)
    padre = models.CharField(max_length=50, blank=True, null=True)
    madre = models.CharField(max_length=50, blank=True, null=True)
    conyuge = models.CharField(max_length=50, blank=True, null=True)
    hijos = models.CharField(max_length=100, blank=True, null=True)
    num_acta = models.IntegerField(blank=True, null=True)
    num_libro = models.IntegerField(blank=True, null=True)
    num_hoja = models.IntegerField(blank=True, null=True)
    num_ano = models.IntegerField(blank=True, null=True)
    num_cartilla_smn = models.CharField(max_length=15, blank=True, null=True)
    ano_clase = models.IntegerField(blank=True, null=True)
    pigmentacion = models.CharField(max_length=1, blank=True, null=True)
    pelo = models.CharField(max_length=1, blank=True, null=True)
    frente = models.CharField(max_length=1, blank=True, null=True)
    cejas = models.CharField(max_length=1, blank=True, null=True)
    ojos = models.CharField(max_length=1, blank=True, null=True)
    nariz = models.CharField(max_length=1, blank=True, null=True)
    boca = models.CharField(max_length=1, blank=True, null=True)
    estaturamts = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    pesokg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    senas_visibles = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=30, blank=True, null=True)
    pasaporte = models.CharField(max_length=40, blank=True, null=True)
    fm = models.CharField(max_length=30, blank=True, null=True)
    inicio_vigencia = models.DateTimeField(blank=True, null=True)
    termino_vigencia = models.DateTimeField(blank=True, null=True)
    entrada_salida = models.CharField(max_length=1, blank=True, null=True)
    observaciones_empleado = models.CharField(max_length=255, blank=True, null=True)
    area_academica = models.CharField(max_length=6, blank=True, null=True)
    tipo_personal = models.CharField(max_length=1, blank=True, null=True)
    tipo_control = models.CharField(max_length=1, blank=True, null=True)
    rfc2 = models.CharField(max_length=13, blank=True, null=True)
    tipo_trabajador = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'