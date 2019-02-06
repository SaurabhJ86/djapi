# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-06 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import status.models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=status.models.upload_image),
        ),
    ]
