# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-02 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis_codes', '0002_auto_20190301_1518'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Code',
            new_name='DiagnosisCode',
        ),
    ]
