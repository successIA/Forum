# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-30 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0013_auto_20190629_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='threadrevision',
            name='marked_message',
            field=models.TextField(blank=True),
        ),
    ]
