# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 06:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0004_auto_20160321_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='is_dirty',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='network',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='router',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 21, 6, 30, 16, 414423, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='router',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 21, 6, 30, 16, 414470, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]