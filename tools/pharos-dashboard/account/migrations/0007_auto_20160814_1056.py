# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 10:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20160813_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='gpgkey',
            new_name='pgpkey',
        ),
    ]