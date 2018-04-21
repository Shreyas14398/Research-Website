# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-21 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0007_auto_20180408_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_det',
            name='category',
            field=models.CharField(default='OC', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal_det',
            name='pemail',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal_det',
            name='phno',
            field=models.PositiveIntegerField(default=1234),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal_det',
            name='retitle',
            field=models.CharField(default='TEST', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal_det',
            name='typet',
            field=models.CharField(default='Full-Time', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='su_personal_det',
            name='affiliation',
            field=models.CharField(default='Private', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='su_personal_det',
            name='institution',
            field=models.CharField(default='SASTRA', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='su_personal_det',
            name='pemail',
            field=models.EmailField(default='abcd@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='su_personal_det',
            name='phno',
            field=models.PositiveIntegerField(default=23456),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supervisor',
            name='external',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dc_meeting',
            name='progress',
            field=models.CharField(choices=[('A', 'Zeroth Review'), ('B', 'First DC'), ('C', 'Coursework Completion'), ('D', 'Comprehensive Viva'), ('E', 'RAC'), ('F', 'Second DC'), ('G', 'Thesis Submission'), ('H', 'Open Defence')], default='A', max_length=30),
        ),
    ]
