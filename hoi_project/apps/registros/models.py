# -*- coding: utf-8 -*-
from django.db import models
from datetime import date


class Proyectos(models.Model):
    proyecto = models.ForeignKey('voluntariado.Proyecto')
    voluntario = models.ForeignKey('voluntariado.Voluntario')
    horas = models.PositiveIntegerField(default=0)
    fecha = models.DateField(default=date.today)
    actividad = models.CharField('Actividad', max_length=200)

    class Meta:
        verbose_name = "Registro de proyecto"
        verbose_name_plural = "Registro de proyectos"

    def __unicode__(self):
        return unicode(self.proyecto.titulo)


class Servicios(models.Model):
    servicio = models.ForeignKey('voluntariado.Servicio')
    voluntario = models.ForeignKey('voluntariado.Voluntario')
    horas = models.PositiveIntegerField(default=0)
    fecha = models.DateField(default=date.today)
    actividad = models.CharField('Actividad', max_length=200)

    class Meta:
        verbose_name = "Registro de servicio"
        verbose_name_plural = "Registro de servicios"

    def __unicode__(self):
        return unicode(self.servicio.servicio)
