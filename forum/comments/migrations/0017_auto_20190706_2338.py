# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-06 22:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0016_auto_20190630_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='downvoters',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='upvoters',
        ),
    ]
