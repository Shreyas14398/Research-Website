# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-17 10:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0014_reports'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupMess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000)),
                ('regno', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(0)])),
                ('mid', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]