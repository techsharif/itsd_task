# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-04 02:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20171003_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='the_date',
        ),
    ]
