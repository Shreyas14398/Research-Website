# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Research.forms import LoginS
from Research.forms import LoginSu
from Research.forms import LoginD
from Research.models import Scholar
from Research.models import Supervisor

# Create your views here.

def home(request):
  return render(request,"home.html",{})

def logins(request):
  if request.POST:
    MyUseForm=LoginS(request.POST)
    if MyUseForm.is_valid():
     dbN=Scholar.objects.get(regno=MyUseForm.cleaned_data['regno'])
     request.session['regno']=dbN.regno
     return render(request,"home.html",{"name":dbN.name})
    else:
     return render(request,"login.html",{"message":"Invalid Username or Password"}) 
  else:
    return render(request,"login.html",{})

def loginsu(request): 
  if request.POST:
    MyUseForm=LoginSu(request.POST)
    if MyUseForm.is_valid():
      dbN=Supervisor.objects.get(mid=MyUseForm.cleaned_data['mid'])
      request.session['mid']=dbN.mid
      return render(request,'home.html',{"name":dbN.name})
    else:
      return render(request,"login.html",{"message":"Invalid Username or Password"})
  else:
    return render(request,"login.html",{})

def logind(request): 
  if request.POST:
    MyUseForm=LoginD(request.POST)
    if MyUseForm.is_valid():
      dbN=Supervisor.objects.get(mid=MyUseForm.cleaned_data['mid'])
      request.session['mid']=dbN.mid
      return render(request,'home.html',{"name":dbN.name})
    else:
      return render(request,"login.html",{"message":"Invalid Username or Password"})
  else:
    return render(request,"login.html",{})

def superm(request):
   return render(request,"super.html",{})

def super1(request):
   return render(request,"super1.html",{})

def super2(request):
   return render(request,"super2.html",{})

def super3(request):
   return render(request,"super3.html",{})

def super4(request):
   return render(request,"super4.html",{})
 
def support(request):
   return render(request,"support.html",{})
