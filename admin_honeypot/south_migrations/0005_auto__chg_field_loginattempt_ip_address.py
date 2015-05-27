# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LoginAttempt.ip_address'
        db.alter_column(u'admin_honeypot_loginattempt', 'ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True))

    def backwards(self, orm):

        # Changing field 'LoginAttempt.ip_address'
        db.alter_column(u'admin_honeypot_loginattempt', 'ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True))

    models = {
        u'admin_honeypot.loginattempt': {
            'Meta': {'ordering': "('timestamp',)", 'object_name': 'LoginAttempt'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['admin_honeypot']