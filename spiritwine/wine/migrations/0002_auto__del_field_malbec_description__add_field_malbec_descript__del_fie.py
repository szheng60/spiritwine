# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Malbec.description'
        db.delete_column('wine_malbec', 'description')

        # Adding field 'Malbec.descript'
        db.add_column('wine_malbec', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'CabernetSauvignon.description'
        db.delete_column('wine_cabernetsauvignon', 'description')

        # Adding field 'CabernetSauvignon.descript'
        db.add_column('wine_cabernetsauvignon', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Sake.description'
        db.delete_column('wine_sake', 'description')

        # Adding field 'Sake.descript'
        db.add_column('wine_sake', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Gin.description'
        db.delete_column('wine_gin', 'description')

        # Adding field 'Gin.descript'
        db.add_column('wine_gin', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Brandy.description'
        db.delete_column('wine_brandy', 'description')

        # Adding field 'Brandy.descript'
        db.add_column('wine_brandy', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Vodka.description'
        db.delete_column('wine_vodka', 'description')

        # Adding field 'Vodka.descript'
        db.add_column('wine_vodka', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Whiskey.description'
        db.delete_column('wine_whiskey', 'description')

        # Adding field 'Whiskey.descript'
        db.add_column('wine_whiskey', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Merlot.description'
        db.delete_column('wine_merlot', 'description')

        # Adding field 'Merlot.descript'
        db.add_column('wine_merlot', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Rum.description'
        db.delete_column('wine_rum', 'description')

        # Adding field 'Rum.descript'
        db.add_column('wine_rum', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'PinotNoir.description'
        db.delete_column('wine_pinotnoir', 'description')

        # Adding field 'PinotNoir.descript'
        db.add_column('wine_pinotnoir', 'descript',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Malbec.description'
        db.add_column('wine_malbec', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Malbec.descript'
        db.delete_column('wine_malbec', 'descript')

        # Adding field 'CabernetSauvignon.description'
        db.add_column('wine_cabernetsauvignon', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'CabernetSauvignon.descript'
        db.delete_column('wine_cabernetsauvignon', 'descript')

        # Adding field 'Sake.description'
        db.add_column('wine_sake', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Sake.descript'
        db.delete_column('wine_sake', 'descript')

        # Adding field 'Gin.description'
        db.add_column('wine_gin', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Gin.descript'
        db.delete_column('wine_gin', 'descript')

        # Adding field 'Brandy.description'
        db.add_column('wine_brandy', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Brandy.descript'
        db.delete_column('wine_brandy', 'descript')

        # Adding field 'Vodka.description'
        db.add_column('wine_vodka', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Vodka.descript'
        db.delete_column('wine_vodka', 'descript')

        # Adding field 'Whiskey.description'
        db.add_column('wine_whiskey', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Whiskey.descript'
        db.delete_column('wine_whiskey', 'descript')

        # Adding field 'Merlot.description'
        db.add_column('wine_merlot', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Merlot.descript'
        db.delete_column('wine_merlot', 'descript')

        # Adding field 'Rum.description'
        db.add_column('wine_rum', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Rum.descript'
        db.delete_column('wine_rum', 'descript')

        # Adding field 'PinotNoir.description'
        db.add_column('wine_pinotnoir', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)

        # Deleting field 'PinotNoir.descript'
        db.delete_column('wine_pinotnoir', 'descript')


    models = {
        'wine.brandy': {
            'Meta': {'object_name': 'Brandy'},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'wine.cabernetsauvignon': {
            'Meta': {'object_name': 'CabernetSauvignon'},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'wine.gin': {
            'Meta': {'object_name': 'Gin'},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'flavor': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'wine.malbec': {
            'Meta': {'object_name': 'Malbec', 'ordering': "['name']"},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'wine.merlot': {
            'Meta': {'object_name': 'Merlot'},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'wine.pinotnoir': {
            'Meta': {'object_name': 'PinotNoir'},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'wine.rum': {
            'Meta': {'object_name': 'Rum'},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'flavor': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'wine.sake': {
            'Meta': {'object_name': 'Sake'},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'wine.vodka': {
            'Meta': {'object_name': 'Vodka'},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'wine.whiskey': {
            'Meta': {'object_name': 'Whiskey'},
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'descript': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '15', 'default': '0'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['wine']