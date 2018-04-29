# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.
class Scholar(models.Model):
   regno=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   password=models.CharField(max_length=30)

class Personal_Det(models.Model):
   name=models.CharField(max_length=30)
   regno=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   email=models.EmailField()
   pemail=models.EmailField()
   category=models.CharField(max_length=10)
   school=models.CharField(max_length=30)
   phno=models.PositiveIntegerField()
   retitle=models.CharField(max_length=500)
   typet=models.CharField(max_length=30)
   regdate=models.CharField(max_length=10)
   sex=models.CharField(max_length=10)
   dob=models.CharField(max_length=10)
   supervisor=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])


class Supervisor(models.Model):
   mid=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   password=models.CharField(max_length=30)
   dean=models.BooleanField(default=False)
   external=models.BooleanField(default=False)
   
class Su_Personal_Det(models.Model):
   name=models.CharField(max_length=30)
   mid=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   phno=models.PositiveIntegerField()
   email=models.EmailField()
   pemail=models.EmailField()
   sex=models.CharField(max_length=10)
   school=models.CharField(max_length=30)
   aoi=models.CharField(max_length=500)
   institution=models.CharField(max_length=500)
   designation=models.CharField(max_length=300)

class DC_Meeting(models.Model):
   Progress_Choices=(
        ("A","Zeroth Review"),
        ("B","First DC"),
        ("C","Coursework Completion"),
        ("D","Comprehensive Viva"),
        ("E","RAC"),
        ("F","Second DC"),
        ("G","Thesis Submission"),
        ("H","Open Defence"),
   )
   progress=models.CharField(choices=Progress_Choices,default="A",max_length=30)
   remarks=models.CharField(max_length=500)
   message=models.CharField(max_length=500)
   status=models.CharField(max_length=30,default="None")
   sdate=models.DateField(null=True,blank=True)
   cdate=models.DateField(null=True,blank=True)
   Completed=models.BooleanField(default=False)
   Started=models.BooleanField(default=False)
   regno=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
  
class Publications(models.Model):
   title=models.CharField(max_length=1000)
   name=models.CharField(max_length=1000)
   date=models.CharField(max_length=10)
   author=models.CharField(max_length=1000)
   regno=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   mid=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])

class Announcement(models.Model):
  title=models.CharField(max_length=200)
  body=models.CharField(max_length=1000)
  adate=models.DateField(null=True,blank=True)

class DCM(models.Model):
  mid=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
  regno=models.PositiveIntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
  name=models.CharField(max_length=30)
  institution=models.CharField(max_length=500)
   
   
   
