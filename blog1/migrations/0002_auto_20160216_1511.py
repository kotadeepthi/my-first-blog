# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='test',
            new_name='text',
        ),
    ]
