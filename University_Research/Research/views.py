# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Research.forms import LoginS
from Research.forms import LoginSu
from Research.forms import LoginD
from Research.models import Scholar
from Research.models import Supervisor

# Create your views here.

def logins(request):
  if request.POST:
    MyUseForm=LoginS(request.POST)
    if MyUseForm.is_valid():
     dbN=Scholar.objects.get(regno=MyUseForm.cleaned_data['regno'])
     request.session['regno']=regno
     return render(request,'main1.html',{"name":dbN.name})
    else:
     return render(request,"base.html",{"message":"Invalid Username or Password"}) 
  else:
    return render(request,'base.html',{})

def loginsu(request): 
  if request.POST:
    MyUseForm=LoginSu(request.POST)
    if MyUseForm.is_valid():
      dbN=Supervisor.objects.get(mid=MyUseForm.cleaned_data['mid'])
      request.session['mid']=mid
      return render(request,'main1.html',{"name":dbN.name})
    else:
      return render(request,"base.html",{"message":"Invalid Username or Password"})
  else:
    return render(request,"base.html",{})

def logind(request): 
  if request.POST:
    MyUseForm=LoginD(request.POST)
    if MyUseForm.is_valid():
      dbN=Supervisor.objects.get(mid=MyUseForm.cleaned_data['mid'])
      request.session['mid']=mid
      return render(request,'main1.html',{"name":dbN.name})
    else:
      return render(request,"base.html",{"message":"Invalid Username or Password"})
  else:
    return render(request,"base.html",{})


 

