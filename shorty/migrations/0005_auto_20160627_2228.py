# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorty', '0004_auto_20160627_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='desktopRedirectCount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='mobileRedirectCount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='tabletRedirectCount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
