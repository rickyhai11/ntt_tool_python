# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0005_auto_20160413_0637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endpoint',
            old_name='endpoint_ip_address',
            new_name='ip_address',
        ),
        migrations.RenameField(
            model_name='endpoint',
            old_name='endpoint_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='endpoint',
            old_name='endpoint_status',
            new_name='status',
        ),
    ]