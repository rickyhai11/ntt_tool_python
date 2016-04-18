# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrafficTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_on', models.DateTimeField()),
                ('traffic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.Traffic')),
            ],
        ),
    ]
