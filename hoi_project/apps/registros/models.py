# -*- coding: utf-8 -*-
from django.db import models
from datetime import date


class Proyectos(models.Model):
    proyecto = models.ForeignKey('proyectos_academicos.Proyecto')
    voluntario = models.ForeignKey('proyectos_academicos.Voluntario')
    horas = models.PositiveIntegerField(default=0)
    fecha = models.DateField(default=date.today)
    actividad = models.CharField('Actividad', max_length=200)

    class Meta:
        verbose_name = "Registro de horas"
        verbose_name_plural = "Registro de horas"

    def __unicode__(self):
        return unicode(self.proyecto.titulo)


#class Servicios(models.Model):
#    servicio = models.ForeignKey('proyectos_academicos.Servicio')
#    voluntario = models.ForeignKey('proyectos_academicos.Voluntario')
#    horas = models.PositiveIntegerField(default=0)
#    fecha = models.DateField(default=date.today)
#    actividad = models.CharField('Actividad', max_length=200)

#    class Meta:
#        verbose_name = "Registro de servicio"
#        verbose_name_plural = "Registro de servicios"

#    def __unicode__(self):
#        return unicode(self.servicio.servicio)
