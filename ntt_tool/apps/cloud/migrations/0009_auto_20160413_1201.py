# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0008_auto_20160413_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trafficnetworksmap',
            old_name='count',
            new_name='endpoint_count',
        ),
    ]
