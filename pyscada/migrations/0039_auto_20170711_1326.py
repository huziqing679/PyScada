# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0038_auto_20170707_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicewritetask',
            old_name='fineshed',
            new_name='finished',
        ),
    ]