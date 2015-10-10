# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proyectos'
        db.create_table(u'registros_proyectos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voluntariado.Proyecto'])),
            ('voluntario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voluntariado.Voluntario'])),
            ('horas', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('actividad', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'registros', ['Proyectos'])

        # Adding model 'Servicios'
        db.create_table(u'registros_servicios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voluntariado.Servicio'])),
            ('voluntario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voluntariado.Voluntario'])),
            ('horas', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('actividad', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'registros', ['Servicios'])


    def backwards(self, orm):
        # Deleting model 'Proyectos'
        db.delete_table(u'registros_proyectos')

        # Deleting model 'Servicios'
        db.delete_table(u'registros_servicios')


    models = {
        u'registros.proyectos': {
            'Meta': {'object_name': 'Proyectos'},
            'actividad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'horas': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Proyecto']"}),
            'voluntario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Voluntario']"})
        },
        u'registros.servicios': {
            'Meta': {'object_name': 'Servicios'},
            'actividad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'horas': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Servicio']"}),
            'voluntario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Voluntario']"})
        },
        u'voluntariado.categoriasproyecto': {
            'Meta': {'object_name': 'CategoriasProyecto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'voluntariado.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'coordinador': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nucleo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'telefonos': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'voluntariado.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'categorias': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.CategoriasProyecto']", 'null': 'True', 'blank': 'True'}),
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tutor': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'voluntariado.servicio': {
            'Meta': {'object_name': 'Servicio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'voluntariado.voluntario': {
            'CI': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Voluntario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grado_instruccion': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'default': "'imagenes/ninguna.png'", 'max_length': '100'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Institucion']", 'blank': 'True'}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'}),
            'telefono_celular': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['registros']