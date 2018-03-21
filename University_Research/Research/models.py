# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Scholar(models.Model):
   name=models.CharField(max_length=30)
   email=models.CharField(max_length=40)
   regno=models.IntegerField(validators=[MaxValueValidator(999999999)])
   password=models.CharField(max_length=30)
   school=models.CharField(max_length=30)

class Supervisor(models.Model):
   name=models.CharField(max_length=30)
   email=models.CharField(max_length=40)
   mid=models.IntegerField(validators=[MaxValueValidator(999999999)])
   password=models.CharField(max_length=30)
   dean=models.BooleanField()
   school=models.CharField(max_length=30)