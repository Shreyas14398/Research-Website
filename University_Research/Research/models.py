# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Scholar(models.Model):
   regno=models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   password=models.CharField(max_length=30)

class Personal_Det(models.Model):
   name=models.CharField(max_length=30)
   regno=models.OneToOneField(Scholar, primary_key=True)
   email=models.EmailField()
   school=models.CharField(max_length=30)

class Research_Det(models.Model):
   regno=models.OneToOneField(Scholar, primary_key=True)
   supervisor=models.ForeignKey("Supervisor")
   

class Supervisor(models.Model):
   mid=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   password=models.CharField(max_length=30)
   dean=models.BooleanField()
   
class Su_Personal_Det(models.Model):
   name=models.CharField(max_length=30)
   email=models.EmailField()
   school=models.CharField(max_length=30)

class DC_Meeting(models.Model):
   Progress_Choices=(
        (0,"Zeroth Review"),
        (1,"First DC"),
        (2,"Coursework Completion"),
        (3,"Comprehensive Viva"),
        (4,"Second DC"),
        (5,"RAC"),
        (6,"Thesis Submission"),
        (7,"Public Viva"),
   )
   progress=models.CharField(choices=Progress_Choices,default=0,max_length=30)
   remarks=models.CharField(max_length=500)
   status=models.CharField(max_length=30)
   date=models.DateTimeField()
   Completed=models.BooleanField()
   Started=models.BooleanField()
   scholar=models.ManyToManyField("Scholar")
  
class Publications(models.Model):
   title=models.CharField(max_length=1000)
   name=models.CharField(max_length=1000)
   date=models.DateField()
   author=models.ManyToManyField("Scholar")
   author1=models.ManyToManyField("Supervisor")

   
   
   
