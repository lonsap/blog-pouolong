# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
