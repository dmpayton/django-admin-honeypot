# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_honeypot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginattempt',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, verbose_name='ip address', blank=True),
        ),
    ]
