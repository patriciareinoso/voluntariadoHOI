# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategoriasProyecto'
        db.create_table(u'voluntariado_categoriasproyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'voluntariado', ['CategoriasProyecto'])

        # Adding field 'Proyecto.descripcion'
        db.add_column(u'voluntariado_proyecto', 'descripcion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Proyecto.tutor'
        db.add_column(u'voluntariado_proyecto', 'tutor',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Proyecto.categorias'
        db.add_column(u'voluntariado_proyecto', 'categorias',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voluntariado.CategoriasProyecto'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Institucion.nucleo'
        db.add_column(u'voluntariado_institucion', 'nucleo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Institucion.correo_electronico'
        db.add_column(u'voluntariado_institucion', 'correo_electronico',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Institucion.direccion'
        db.add_column(u'voluntariado_institucion', 'direccion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Institucion.telefonos'
        db.add_column(u'voluntariado_institucion', 'telefonos',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Institucion.coordinador'
        db.add_column(u'voluntariado_institucion', 'coordinador',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


        # Changing field 'Voluntario.telefono_casa'
        db.alter_column(u'voluntariado_voluntario', 'telefono_casa', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Voluntario.direccion'
        db.alter_column(u'voluntariado_voluntario', 'direccion', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Voluntario.telefono_celular'
        db.alter_column(u'voluntariado_voluntario', 'telefono_celular', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):
        # Deleting model 'CategoriasProyecto'
        db.delete_table(u'voluntariado_categoriasproyecto')

        # Deleting field 'Proyecto.descripcion'
        db.delete_column(u'voluntariado_proyecto', 'descripcion')

        # Deleting field 'Proyecto.tutor'
        db.delete_column(u'voluntariado_proyecto', 'tutor')

        # Deleting field 'Proyecto.categorias'
        db.delete_column(u'voluntariado_proyecto', 'categorias_id')

        # Deleting field 'Institucion.nucleo'
        db.delete_column(u'voluntariado_institucion', 'nucleo')

        # Deleting field 'Institucion.correo_electronico'
        db.delete_column(u'voluntariado_institucion', 'correo_electronico')

        # Deleting field 'Institucion.direccion'
        db.delete_column(u'voluntariado_institucion', 'direccion')

        # Deleting field 'Institucion.telefonos'
        db.delete_column(u'voluntariado_institucion', 'telefonos')

        # Deleting field 'Institucion.coordinador'
        db.delete_column(u'voluntariado_institucion', 'coordinador')


        # Changing field 'Voluntario.telefono_casa'
        db.alter_column(u'voluntariado_voluntario', 'telefono_casa', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=20))

        # Changing field 'Voluntario.direccion'
        db.alter_column(u'voluntariado_voluntario', 'direccion', self.gf('django.db.models.fields.CharField')(max_length=120))

        # Changing field 'Voluntario.telefono_celular'
        db.alter_column(u'voluntariado_voluntario', 'telefono_celular', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=20))

    models = {
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
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'voluntariado.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'categorias': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.CategoriasProyecto']", 'null': 'True', 'blank': 'True'}),
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
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
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grado_instruccion': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'default': "'imagenes/ninguna.png'", 'max_length': '100'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['voluntariado.Institucion']"}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['voluntariado']