# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0015_supmess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dc_meeting',
            name='regno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='dcm',
            name='regno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='personal_det',
            name='regno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='publications',
            name='regno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='reports',
            name='regno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='scholar',
            name='regno',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='supmess',
            name='regno',
            field=models.CharField(max_length=17),
        ),
    ]
