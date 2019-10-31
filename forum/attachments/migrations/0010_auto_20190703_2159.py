# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-03 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190702_0200'),
        ('attachments', '0009_auto_20190702_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='userprofile',
        ),
        migrations.AddField(
            model_name='attachment',
            name='userprofile',
            field=models.ManyToManyField(blank=True, to='accounts.UserProfile'),
        ),
    ]
