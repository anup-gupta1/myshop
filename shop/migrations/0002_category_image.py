# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category/%Y/%m/%d'),
        ),
    ]
