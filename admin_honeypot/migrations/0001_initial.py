# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255, null=True, verbose_name='username', blank=True)),
                ('ip_address', models.IPAddressField(null=True, verbose_name='ip address', blank=True)),
                ('session_key', models.CharField(max_length=50, null=True, verbose_name='session key', blank=True)),
                ('user_agent', models.TextField(null=True, verbose_name='user-agent', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('path', models.TextField(null=True, verbose_name='path', blank=True)),
            ],
            options={
                'ordering': ('timestamp',),
                'verbose_name': 'login attempt',
                'verbose_name_plural': 'login attempts',
            },
            bases=(models.Model,),
        ),
    ]
