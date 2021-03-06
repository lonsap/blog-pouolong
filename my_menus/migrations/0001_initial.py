# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-30 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_rue', models.CharField(max_length=255)),
                ('code_postal', models.CharField(max_length=6)),
                ('commune', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('adr_mail', models.CharField(max_length=50)),
                ('carte', models.ImageField(upload_to='#')),
            ],
        ),
        migrations.CreateModel(
            name='My_menus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('langue', models.CharField(max_length=200)),
                ('menu_blog', models.CharField(max_length=200)),
                ('menu_lst_boite', models.CharField(max_length=200)),
                ('menu_faq', models.CharField(max_length=200)),
                ('menu_news', models.CharField(max_length=200)),
                ('menu_contacts', models.CharField(max_length=200)),
            ],
        ),
    ]
