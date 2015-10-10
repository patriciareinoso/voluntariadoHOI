# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Institucion'
        db.create_table(u'voluntariado_institucion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'voluntariado', ['Institucion'])

        # Adding model 'Voluntario'
        db.create_table(u'voluntariado_voluntario', (
            ('CI', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('primer_nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('lugar_nacimiento', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('telefono_casa', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=20)),
            ('telefono_celular', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=20)),
            ('correo_electronico', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('institucion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voluntariado.Institucion'], blank=True)),
            ('grado_instruccion', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(default='imagenes/ninguna.png', max_length=100)),
        ))
        db.send_create_signal(u'voluntariado', ['Voluntario'])

        # Adding model 'Proyecto'
        db.create_table(u'voluntariado_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('especialidad', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('dependencia', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('estatus', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'voluntariado', ['Proyecto'])

        # Adding model 'Servicio'
        db.create_table(u'voluntariado_servicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('turno', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'voluntariado', ['Servicio'])


    def backwards(self, orm):
        # Deleting model 'Institucion'
        db.delete_table(u'voluntariado_institucion')

        # Deleting model 'Voluntario'
        db.delete_table(u'voluntariado_voluntario')

        # Deleting model 'Proyecto'
        db.delete_table(u'voluntariado_proyecto')

        # Deleting model 'Servicio'
        db.delete_table(u'voluntariado_servicio')


    models = {
        u'voluntariado.institucion': {
            'Meta': {'object_name': 'Institucion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'voluntariado.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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

    complete_apps = ['voluntariado']
