# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Malbec'
        db.create_table('wine_malbec', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('wine', ['Malbec'])

        # Adding model 'Merlot'
        db.create_table('wine_merlot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('wine', ['Merlot'])

        # Adding model 'CabernetSauvignon'
        db.create_table('wine_cabernetsauvignon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('wine', ['CabernetSauvignon'])

        # Adding model 'PinotNoir'
        db.create_table('wine_pinotnoir', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('wine', ['PinotNoir'])

        # Adding model 'Vodka'
        db.create_table('wine_vodka', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('wine', ['Vodka'])

        # Adding model 'Whiskey'
        db.create_table('wine_whiskey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('wine', ['Whiskey'])

        # Adding model 'Rum'
        db.create_table('wine_rum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('flavor', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
        ))
        db.send_create_signal('wine', ['Rum'])

        # Adding model 'Sake'
        db.create_table('wine_sake', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('wine', ['Sake'])

        # Adding model 'Brandy'
        db.create_table('wine_brandy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('wine', ['Brandy'])

        # Adding model 'Gin'
        db.create_table('wine_gin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=15, default=0, decimal_places=2)),
            ('region', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
            ('produced_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('flavor', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=30)),
        ))
        db.send_create_signal('wine', ['Gin'])


    def backwards(self, orm):
        # Deleting model 'Malbec'
        db.delete_table('wine_malbec')

        # Deleting model 'Merlot'
        db.delete_table('wine_merlot')

        # Deleting model 'CabernetSauvignon'
        db.delete_table('wine_cabernetsauvignon')

        # Deleting model 'PinotNoir'
        db.delete_table('wine_pinotnoir')

        # Deleting model 'Vodka'
        db.delete_table('wine_vodka')

        # Deleting model 'Whiskey'
        db.delete_table('wine_whiskey')

        # Deleting model 'Rum'
        db.delete_table('wine_rum')

        # Deleting model 'Sake'
        db.delete_table('wine_sake')

        # Deleting model 'Brandy'
        db.delete_table('wine_brandy')

        # Deleting model 'Gin'
        db.delete_table('wine_gin')


    models = {
        'wine.brandy': {
            'Meta': {'object_name': 'Brandy'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'wine.cabernetsauvignon': {
            'Meta': {'object_name': 'CabernetSauvignon'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'wine.gin': {
            'Meta': {'object_name': 'Gin'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'flavor': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'wine.malbec': {
            'Meta': {'ordering': "['name']", 'object_name': 'Malbec'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'wine.merlot': {
            'Meta': {'object_name': 'Merlot'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'wine.pinotnoir': {
            'Meta': {'object_name': 'PinotNoir'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'wine.rum': {
            'Meta': {'object_name': 'Rum'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'flavor': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'wine.sake': {
            'Meta': {'object_name': 'Sake'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'wine.vodka': {
            'Meta': {'object_name': 'Vodka'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        },
        'wine.whiskey': {
            'Meta': {'object_name': 'Whiskey'},
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'default': '0', 'decimal_places': '2'}),
            'produced_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['wine']