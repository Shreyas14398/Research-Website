# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.
class Scholar(models.Model):
   regno=models.CharField(max_length=17)
   password=models.CharField(max_length=30)

class Personal_Det(models.Model):
   name=models.CharField(max_length=30)
   lname=models.CharField(max_length=30)
   regno=models.CharField(max_length=17)
   email=models.EmailField()
   pemail=models.EmailField()
   category=models.CharField(max_length=10)
   school=models.CharField(max_length=30)
   phno=models.CharField(max_length=11)
   retitle=models.CharField(max_length=500)
   typet=models.CharField(max_length=30)
   regdate=models.CharField(max_length=10)
   sex=models.CharField(max_length=10)
   dob=models.CharField(max_length=10)
   supervisor=models.CharField(max_length=15)


class Supervisor(models.Model):
   mid=models.CharField(max_length=15)
   password=models.CharField(max_length=30)
   dean=models.BooleanField(default=False)
   external=models.BooleanField(default=False)

class Su_Personal_Det(models.Model):
   name=models.CharField(max_length=30)
   lname=models.CharField(max_length=30)
   mid=models.CharField(max_length=15)
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
   regno=models.CharField(max_length=17)

class Publications(models.Model):
   title=models.CharField(max_length=1000)
   name=models.CharField(max_length=1000)
   date=models.CharField(max_length=10)
   author=models.CharField(max_length=1000)
   regno=models.CharField(max_length=17)
   mid=models.CharField(max_length=15)

class Announcement(models.Model):
  title=models.CharField(max_length=200)
  body=models.CharField(max_length=1000)
  adate=models.DateField(null=True,blank=True)

class DCM(models.Model):
  mid=models.CharField(max_length=15)
  regno=models.CharField(max_length=17)
  name=models.CharField(max_length=30)
  institution=models.CharField(max_length=500)

class Reports(models.Model):
  head=models.CharField(max_length=100)
  body=models.CharField(max_length=1000)
  regno=models.CharField(max_length=17)

class SupMess(models.Model):
  head=models.CharField(max_length=100)
  body=models.CharField(max_length=1000)
  regno=models.CharField(max_length=17)
  mid=models.CharField(max_length=15)
