# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-24 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0010_thread_starting_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=4000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='threads.Thread')),
            ],
        ),
    ]
