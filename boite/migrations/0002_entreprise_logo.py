# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos/'),
        ),
    ]
