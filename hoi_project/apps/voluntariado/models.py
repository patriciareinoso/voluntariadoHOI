# -*- coding: utf-8 -*-
from django.db import models
from apps.registros.models import Proyectos, Servicios


class Institucion(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    nucleo = models.CharField('Núcleo', max_length=30, blank=True)
    correo_electronico = models.CharField('Correo', max_length=30, blank=True)
    direccion = models.CharField('Dirección', max_length=100, blank=True)
    telefonos = models.CharField('Teléfonos', max_length=200, blank=True)

    coordinador = models.CharField('Coordinador', max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Instituciones"

    def __unicode__(self):
        return unicode(self.nombre)

    def horas_mes(self, mes, ano):
        """ Genera el reporte de horas mensuales """
        proyectos = Proyectos.objects.all().filter(
            voluntario__institucion__nombre=self.nombre,
            fecha__month=mes,
            fecha__year=ano)
        counter = 0
        for p in proyectos:
            counter += p.horas
        return (proyectos, counter)

    def horas_ano(self, ano):
        """ Genera el reporte de horas anuales """
        proyectos = Proyectos.objects.all().filter(
            voluntario__institucion__nombre=self.nombre,
            fecha__year=ano)

        horas_ano = 0
        resultado = []
        for mes in range(1, 13):
            proyectos_mes = []
            horas_mes = 0
            for p in proyectos:
                if p.fecha.month == mes:
                    horas_ano += p.horas
                    horas_mes += p.horas
                    proyectos_mes.append(p)
            resultado.append((proyectos_mes, horas_mes))

        return (resultado, horas_ano)


class Voluntario(models.Model):

    class Meta:
        verbose_name = "Pasante"
        verbose_name_plural = "Pasantes"

    OPCIONES_GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    OPCIONES_ESTADO_CIVIL = (
        ('C', 'Casado'),
        ('S', 'Soltero'),
        ('D', 'Divorciado'),
        ('V', 'Viudo'),
    )

    OPCIONES_INSTRUCCION = (
        ('P', 'Educación Primaria'),
        ('M', 'Educación Media'),
        ('S', 'Educación Superior'),
    )

    # Informacion personal del voluntario
    CI = models.CharField('Cédula de identidad',
                          max_length=10, primary_key=True)
    primer_nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    lugar_nacimiento = models.CharField('Lugar de nacimiento',
                                        max_length=30, blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=True)
    genero = models.CharField('Genero', max_length=1, choices=OPCIONES_GENERO)
    ocupacion = models.CharField('Ocupación', max_length=30)
    estado_civil = models.CharField('Estado civil', max_length=1,
                                    choices=OPCIONES_ESTADO_CIVIL)
    # Informacion de contacto
    direccion = models.CharField(
        'Dirección de habitación', max_length=200, blank=True)
    telefono_casa = models.CharField(
        'Teléfono de habitación', max_length=30, blank=True)
    telefono_celular = models.CharField('Teléfono celular', max_length=30)
    correo_electronico = models.EmailField('Correo electrónico')

    # Informacion de la institucion
    institucion = models.ForeignKey(Institucion, verbose_name='Institución')
    grado_instruccion = models.CharField(
        'Grado de instrucción', max_length=1, choices=OPCIONES_INSTRUCCION)

    # Imagen
    imagen = models.ImageField(upload_to='imagenes/',
                               default='imagenes/ninguna.png')

    def __unicode__(self):
        return unicode(self.primer_nombre) + ' ' + unicode(self.apellido)

    def horas_mes(self, mes, ano):
        """ Genera el reporte de horas mensuales """
        proyectos = Proyectos.objects.all().filter(
            voluntario__CI=self.CI,
            fecha__month=mes,
            fecha__year=ano)
        counter = 0
        for p in proyectos:
            counter += p.horas
        return (proyectos, counter)

    def horas_ano(self, ano):
        """ Genera el reporte de horas anuales """
        proyectos = Proyectos.objects.all().filter(
            voluntario__CI=self.CI,
            fecha__year=ano)

        horas_ano = 0
        resultado = []
        for mes in range(1, 13):
            proyectos_mes = []
            horas_mes = 0
            for p in proyectos:
                if p.fecha.month == mes:
                    horas_ano += p.horas
                    horas_mes += p.horas
                    proyectos_mes.append(p)
            resultado.append((proyectos_mes, horas_mes))

        return (resultado, horas_ano)


class CategoriasProyecto(models.Model):

    class Meta:
        verbose_name = "Categoria"

    nombre = models.CharField('Nombre', max_length=50)

    def __unicode__(self):
        return unicode(self.nombre)


class Proyecto(models.Model):

    OPCIONES_ESTATUS = (
        ('P', 'En proceso'),
        ('C', 'Culminado'),
    )

    titulo = models.CharField('Titulo', max_length=30)
    descripcion = models.CharField('Descripción', max_length=200, blank=True)
    tutor = models.CharField('Tutor', max_length=30, blank=True)
    especialidad = models.CharField('Especialidad', max_length=30, blank=True)
    dependencia = models.CharField('Dependencia', max_length=30, blank=True)
    estatus = models.CharField('Estatus', max_length=1,
                               choices=OPCIONES_ESTATUS)
    categorias = models.ForeignKey(CategoriasProyecto, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.titulo)

    def horas_mes(self, mes, ano):
        """ Genera el reporte de horas mensuales """
        proyectos = Proyectos.objects.all().filter(
            proyecto__pk=self.pk,
            fecha__month=mes,
            fecha__year=ano)
        counter = 0
        for p in proyectos:
            counter += p.horas
        return (proyectos, counter)

    def horas_ano(self, ano):
        """ Genera el reporte de horas anuales """
        proyectos = Proyectos.objects.all().filter(
            proyecto__pk=self.pk,
            fecha__year=ano)

        horas_ano = 0
        resultado = []
        for mes in range(1, 13):
            proyectos_mes = []
            horas_mes = 0
            for p in proyectos:
                if p.fecha.month == mes:
                    horas_ano += p.horas
                    horas_mes += p.horas
                    proyectos_mes.append(p)
            resultado.append((proyectos_mes, horas_mes))

        return (resultado, horas_ano)


class Servicio(models.Model):

    OPCIONES_TURNO = (
        ('am', 'A.M.'),
        ('pm', 'P.M.'),
    )

    servicio = models.CharField('Servicio', max_length=30)
    turno = models.CharField('Turno', max_length=2, choices=OPCIONES_TURNO)

    def __unicode__(self):
        return unicode(self.servicio)

    def horas_mes(self, mes, ano):
        """ Genera el reporte de horas mensuales """
        servicios = Servicios.objects.all().filter(
            servicio__pk=self.pk,
            fecha__month=mes,
            fecha__year=ano)
        counter = 0
        for p in servicios:
            counter += p.horas
        return (servicios, counter)

    def horas_ano(self, ano):
        """ Genera el reporte de horas anuales """
        servicios = Servicios.objects.all().filter(
            servicio__pk=self.pk,
            fecha__year=ano)

        horas_ano = 0
        resultado = []
        for mes in range(1, 13):
            servicios_mes = []
            horas_mes = 0
            for p in servicios:
                if p.fecha.month == mes:
                    horas_ano += p.horas
                    horas_mes += p.horas
                    servicios_mes.append(p)
            resultado.append((servicios_mes, horas_mes))

        return (resultado, horas_ano)
