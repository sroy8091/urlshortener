# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcode', '0002_auto_20161215_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]