# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Institucion'
        db.create_table('proyectos_academicos_institucion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nucleo', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('correo_electronico', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('direccion', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
            ('telefonos', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('coordinador', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50)),
        ))
        db.send_create_signal('proyectos_academicos', ['Institucion'])

        # Adding model 'Voluntario'
        db.create_table('proyectos_academicos_voluntario', (
            ('CI', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=10)),
            ('primer_nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lugar_nacimiento', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('direccion', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('telefono_casa', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('telefono_celular', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('correo_electronico', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('institucion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos_academicos.Institucion'])),
            ('grado_instruccion', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, default='imagenes/ninguna.png')),
        ))
        db.send_create_signal('proyectos_academicos', ['Voluntario'])

        # Adding model 'CategoriasProyecto'
        db.create_table('proyectos_academicos_categoriasproyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('proyectos_academicos', ['CategoriasProyecto'])

        # Adding model 'Proyecto'
        db.create_table('proyectos_academicos_proyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('tutor', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('especialidad', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('dependencia', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('estatus', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('categorias', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['proyectos_academicos.CategoriasProyecto'], null=True)),
        ))
        db.send_create_signal('proyectos_academicos', ['Proyecto'])

        # Adding model 'Servicio'
        db.create_table('proyectos_academicos_servicio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('turno', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('proyectos_academicos', ['Servicio'])


    def backwards(self, orm):
        # Deleting model 'Institucion'
        db.delete_table('proyectos_academicos_institucion')

        # Deleting model 'Voluntario'
        db.delete_table('proyectos_academicos_voluntario')

        # Deleting model 'CategoriasProyecto'
        db.delete_table('proyectos_academicos_categoriasproyecto')

        # Deleting model 'Proyecto'
        db.delete_table('proyectos_academicos_proyecto')

        # Deleting model 'Servicio'
        db.delete_table('proyectos_academicos_servicio')


    models = {
        'proyectos_academicos.categoriasproyecto': {
            'Meta': {'object_name': 'CategoriasProyecto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'proyectos_academicos.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'coordinador': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'correo_electronico': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'direccion': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nucleo': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'})
        },
        'proyectos_academicos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'categorias': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['proyectos_academicos.CategoriasProyecto']", 'null': 'True'}),
            'dependencia': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tutor': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'})
        },
        'proyectos_academicos.servicio': {
            'Meta': {'object_name': 'Servicio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'proyectos_academicos.voluntario': {
            'CI': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '10'}),
            'Meta': {'object_name': 'Voluntario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grado_instruccion': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'imagenes/ninguna.png'"}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos_academicos.Institucion']"}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['proyectos_academicos']