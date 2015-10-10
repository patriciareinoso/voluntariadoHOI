# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
from apps.registros.models import Proyectos, Servicios
from apps.voluntariado.models import Institucion
from apps.registros.actions import export_as_csv_action

# Filters


class InstitucionFilter(SimpleListFilter):
    title = _('Institucion')
    parameter_name = 'institucion'

    def lookups(self, request, model_admin):
        queryset = Institucion.objects.all()
        return queryset.values_list('id', 'nombre')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(voluntario__institucion=self.value())

# Admin Models


class ProyectosAdmin(admin.ModelAdmin):
    search_fields = [
        'proyecto__titulo', 'proyecto__estatus', 'voluntario__primer_nombre',
        'voluntario__apellido',
        'voluntario__CI', 'voluntario__institucion__nombre', 'fecha']
    list_display = [
        'get_proyecto', 'get_proyecto_estatus', 'get_institucion',
        'voluntario', 'get_CI', 'horas', 'fecha']
    list_filter = ['voluntario', 'proyecto', InstitucionFilter, 'fecha']
    actions = [export_as_csv_action("Exportar como CSV",
               fields=['proyecto', 'voluntario', 'horas', 'fecha'])]

    def get_proyecto(self, obj):
        return obj.proyecto.titulo

    get_proyecto.short_description = 'Proyecto'
    get_proyecto.admin_order_field = 'proyecto__titulo'

    def get_proyecto_estatus(self, obj):
        if obj.proyecto.estatus == 'C':
            return 'Culminado'
        else:
            return 'En proceso'

    get_proyecto_estatus.short_description = 'Estatus'
    get_proyecto_estatus.admin_order_field = 'proyecto__estatus'

    def get_institucion(self, obj):
        return obj.voluntario.institucion

    get_institucion.short_description = 'Institucion'
    get_institucion.admin_order_field = 'voluntario__institucion'

    def get_CI(self, obj):
        return obj.voluntario.CI

    get_CI.short_description = 'Cedula'
    get_CI.admin_order_field = 'voluntario__CI'


class ServiciosAdmin(admin.ModelAdmin):
    search_fields = ['servicio__servicio', 'voluntario__primer_nombre',
                     'voluntario__apellido',
                     'voluntario__CI', 'voluntario__institucion__nombre',
                     'fecha']
    list_display = [
        'get_servicio', 'get_institucion', 'voluntario', 'get_CI', 'horas',
        'fecha']
    list_filter = ['voluntario', 'servicio', InstitucionFilter, 'fecha']
    actions = [export_as_csv_action("Exportar como CSV",
               fields=['servicio', 'voluntario', 'horas', 'fecha'])]

    def get_servicio(self, obj):
        return obj.servicio.servicio
    get_servicio.short_description = 'Servicio'
    get_servicio.admin_order_field = 'servicio__servicio'

    def get_institucion(self, obj):
        return obj.voluntario.institucion
    get_institucion.short_description = 'Institucion'
    get_institucion.admin_order_field = 'voluntario__institucion'

    def get_CI(self, obj):
        return obj.voluntario.CI
    get_CI.short_description = 'Cedula'
    get_CI.admin_order_field = 'voluntario__CI'

# Registers

admin.site.register(Proyectos, ProyectosAdmin)
admin.site.register(Servicios, ServiciosAdmin)
