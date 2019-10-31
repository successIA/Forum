# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-06 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import forum.attachments.models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0005_attachment_md5sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='image',
            field=models.ImageField(storage=forum.attachments.models.MediaFileSystemStorage(), upload_to=forum.attachments.models.upload_to),
        ),
    ]
