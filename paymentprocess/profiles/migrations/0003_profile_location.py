# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-21 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my default location', max_length=120),
        ),
    ]
