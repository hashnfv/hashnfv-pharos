# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jenkins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenkinsstatistic',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]