# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_honeypot', '0002_auto_20160208_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginattempt',
            name='record_by_address',
            field=models.TextField(blank=True, null=True, verbose_name='record by address'),
        ),
    ]
