# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boite', '0008_auto_20160403_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='date_evt',
            field=models.DateTimeField(null=True, verbose_name="Date de l'événement"),
        ),
    ]