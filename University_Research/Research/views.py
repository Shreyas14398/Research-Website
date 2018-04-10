# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Research.forms import LoginS
from Research.forms import LoginSu
from Research.forms import LoginD
from Research.models import Scholar
from Research.models import Personal_Det
from Research.models import Su_Personal_Det
from Research.models import Supervisor
from Research.models import Publications
from Research.models import DC_Meeting
from Research.forms import editform
from Research.forms import regnosearchForm
from Research.forms import startform
from Research.forms import infof
import datetime
from Research.forms import namesearchForm
from Research.forms import SunamesearchForm
from Research.forms import midsearchForm
from Research.forms import schregForm
from Research.forms import suregForm

# Create your views here.
levels={"A":"Zeroth Review","B":"First DC","C":"Coursework Completion","D":"Comprehensive Viva","E":"Second DC","F":"RAC","G":"Thesis Submission","H":"Public Viva"}
def home(request):
  return render(request,"home.html",{})

def logins(request):
  if request.POST:
    MyUseForm=LoginS(request.POST)
    if MyUseForm.is_valid():
     dbN=Scholar.objects.get(regno=MyUseForm.cleaned_data['regno'])
     request.session['regno']=dbN.regno
     return HttpResponseRedirect('/scholar1')
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
     return HttpResponseRedirect('/dean1')
    else:
     return render(request,"login.html",{"message":"Invalid Username or Password"}) 
  else:
    return render(request,"login.html",{})

def logout(request):
  try:
    del request.session['regno']
  except:
    pass
  return render(request,"login.html",{"message":"Logged out successfully!"})

def logoutsu(request):
  try:
    del request.session['mid']
  except:
    pass
  return render(request,"login.html",{"message":"Logged out successfully!"})

def loginsu(request): 
  if request.POST:
    MyUseForm=LoginSu(request.POST)
    if MyUseForm.is_valid():
      dbN=Supervisor.objects.get(mid=MyUseForm.cleaned_data['mid'])
      request.session['mid']=dbN.mid
      return HttpResponseRedirect('/supervisor1')
    else:
      return render(request,"login.html",{"message":"Invalid Username or Password"})
  else:
    return render(request,"login.html",{})

def scholar1(request):
  status1=""
  rno=request.session['regno']
  dbP=Personal_Det.objects.get(regno=rno)
  dbPu=Publications.objects.filter(regno=rno).values()
  dbst=DC_Meeting.objects.filter(regno=rno,Completed=False,Started=True).values()
  dbSu=Su_Personal_Det.objects.get(mid=dbP.supervisor)
  dbsp=DC_Meeting.objects.filter(regno=rno).values()
  if dbst.exists():
    status=DC_Meeting.objects.get(regno=rno,Completed=False,Started=True)
    status1=status.get_progress_display()
  return render(request,"scholar1.html",{"name":dbP.name,"dob":dbP.dob,"sex":dbP.sex,"regno":dbP.regno,"regdate":dbP.regdate,"school":dbP.school,"pubs":dbPu,"supervisor":dbSu.name,"status1":status1,"dbsp":dbsp,"levels":levels})

def supervisor1(request):
  mid=request.session['mid']
  dbP=Su_Personal_Det.objects.get(mid=mid)
  dbPu=Publications.objects.filter(mid=mid).values()
  dbSch=Personal_Det.objects.filter(supervisor=mid).values()
  return render(request,"supervisor1.html",{"pubs":dbPu,"sch":dbSch,"name":dbP.name,"email":dbP.email,"sex":dbP.sex,"school":dbP.school,"mid":dbP.mid,"aoi":dbP.aoi})

def suinfo(request):
  if request.POST:
     SuF=midsearchForm(request.POST)
     if SuF.is_valid():
       mid=SuF.cleaned_data['mid']
       dbP=Su_Personal_Det.objects.get(mid=mid)
       dbPu=Publications.objects.filter(mid=mid).values()
       dbSch=Personal_Det.objects.filter(supervisor=mid).values()
       return render(request,"suinfo.html",{"pubs":dbPu,"sch":dbSch,"name":dbP.name,"email":dbP.email,"sex":dbP.sex,"school":dbP.school,"mid":dbP.mid,"aoi":dbP.aoi})
  else:
     return render(request,"home.html",{})  

def schinfo(request):
  status1=""
  if request.POST:
    IForm=infof(request.POST)
    if IForm.is_valid():
      rno=IForm.cleaned_data['regno']
      dbP=Personal_Det.objects.get(regno=rno)
      dbPu=Publications.objects.filter(regno=rno).values()
      dbSu=Su_Personal_Det.objects.get(mid=dbP.supervisor)
      dbst=DC_Meeting.objects.filter(regno=rno,Completed=False,Started=True)
      dbsp=DC_Meeting.objects.filter(regno=rno).values()
      if dbst.exists():
        status=DC_Meeting.objects.get(regno=rno,Completed=False,Started=True)
        status1=status.get_progress_display()
      return render(request,"schinfo.html",{"name":dbP.name,"dob":dbP.dob,"sex":dbP.sex,"regno":dbP.regno,"regdate":dbP.regdate,"school":dbP.school,"pubs":dbPu,"supervisor":dbSu.name,"status1":status1,"dbsp":dbsp,"levels":levels})
    else:
      return render(request,"home.html",{})
  else:
    return render(request,"home.html",{})
 
def schedit(request):
  if request.POST:
    EForm=editform(request.POST)
    if EForm.is_valid():
      dbS=DC_Meeting.objects.get(regno=EForm.cleaned_data['regno'],progress=EForm.cleaned_data['progress'])
      dbS.status=EForm.cleaned_data['status']
      dbS.remarks=EForm.cleaned_data['remarks']
      dbS.cdate=EForm.cleaned_data['date']
      if dbS.status=="Pass":
         dbS.Completed=True
      dbS.save()
      return HttpResponseRedirect('/supervisor1')
    else:
      return render(request,"login.html",{})
  else:
      return render(request,"home.html",{})

def schstart(request):
  if request.POST:
    SForm=startform(request.POST)
    if SForm.is_valid():
      dbS=DC_Meeting.objects.get(regno=SForm.cleaned_data['regno'],progress=SForm.cleaned_data['progress'])
      dbS.sdate=SForm.cleaned_data['date']
      dbS.message=SForm.cleaned_data['message']
      dbS.Started=True
      dbS.save()
      return HttpResponseRedirect('/supervisor1')
    else:
      return render(request,"login.html",{})
  else:
    return render(request,"home.html",{})

def dean1(request):
    mid=request.session['mid']
    dbD=Supervisor.objects.get(mid=mid,dean=True)
    Schcnt=Scholar.objects.filter().count()
    Supcnt=Supervisor.objects.filter().count()-1
    now=datetime.datetime.now()
    if now.hour<12:
      message="Good Morning..."
    elif now.hour>=12 and now.hour<16:
      message="Good Afternoon..."
    else:
      message="Good Evening..."
    return render(request,"dean1.html",{"message":message,"mid":mid,"sch":Schcnt,"sup":Supcnt})

def dean2(request):
  mid=request.session['mid']
  dbD=Supervisor.objects.get(mid=mid,dean=True)
  Schcnt=Scholar.objects.filter().count()
  Supcnt=Supervisor.objects.filter().count()-1
  now=datetime.datetime.now()
  if now.hour<12:
    message="Good Morning..."
  elif now.hour>=12 and now.hour<16:
    message="Good Afternoon..."
  else:
    message="Good Evening..."
  if request.POST:
    SearchF=regnosearchForm(request.POST)
    if SearchF.is_valid():
     rno=SearchF.cleaned_data['regno']
     dbS=Personal_Det.objects.filter(regno=rno).values()
     return render(request,'dean1.html',{"dbS":dbS,"message":message,"mid":mid,"sch":Schcnt,"sup":Supcnt})
    else:
     SearchF=namesearchForm(request.POST)
     if SearchF.is_valid():
       name=SearchF.cleaned_data['regno']
       dbS=Personal_Det.objects.filter(name=name).values()
       return render(request,'dean1.html',{"dbS":dbS,"message":message,"mid":mid,"sch":Schcnt,"sup":Supcnt})
     else:
       return render(request,'dean1.html',{})
  else:
    return render(request,'dean1.html',{})
    
def dean3(request):
    if request.POST:
      SearchF=midsearchForm(request.POST)
      if SearchF.is_valid():
        mid=SearchF.cleaned_data['mid']
        dbSu=Su_Personal_Det.objects.filter(mid=mid).values()
        return render(request,'dean1.html',{"dbSu":dbSu,"message":message,"mid":mid,"sch":Schcnt,"sup":Supcnt})
      else:
        SearchF=SunamesearchForm(request.POST)
        if SearchF.is_valid():
          name=SearchF.cleaned_data['mid']
          dbSu=Su_Personal_Det.objects.filter(name=name).values()
          return render(request,'dean1.html',{"dbSu":dbSu,"message":message,"mid":mid,"sch":Schcnt,"sup":Supcnt})
        else:
          return render(request,'dean1.html',{})
    else:
      return render(request,'dean1.html',{})

def sureg(request):
  if request.POST:
    RegSu=suregForm(request.POST)
    if RegSu.is_valid():
      SuObj=Su_Personal_Det(name=RegSu.cleaned_data['name'],sex=RegSu.cleaned_data['sex'],mid=RegSu.cleaned_data['mid'],school=RegSu.cleaned_data['school'],email=RegSu.cleaned_data['email'],aoi=RegSu.cleaned_data['aoi'])
      SuObj.save()
      SuuObj=Supervisor(mid=RegSu.cleaned_data['mid'],password=RegSu.cleaned_data['mid'])
      SuuObj.save()
      return render(request,"login.html",{"message":"Registered Successfully!"})
    else:
      return render(request,"login.html",{"message":"Couldn't Register!"})
  else:
    return render(request,"home.html",{})

def schreg(request):
  if request.POST:
    RegS=schregForm(request.POST)
    if RegS.is_valid():
      SObj=Personal_Det(name=RegS.cleaned_data['name'],sex=RegS.cleaned_data['sex'],dob=RegS.cleaned_data['dob'],regno=RegS.cleaned_data['regno'],school=RegS.cleaned_data['school'],email=RegS.cleaned_data['email'],supervisor=RegS.cleaned_data['supervisor'],regdate=RegS.cleaned_data['regdate'])
      SObj.save()
      TObj=Scholar(regno=RegS.cleaned_data['regno'],password=RegS.cleaned_data['regno'])
      TObj.save()
      for key,values in levels.iteritems():
        UObj=DC_Meeting(regno=RegS.cleaned_data['regno'],progress=key)
        UObj.save()
      return render(request,"login.html",{"message":"Registered Successfully!"})
    else:
      return render(request,"login.html",{"message":"Couldn't Register!"})
  else:
    return render(request,"home.html",{})

def reg(request):
  return render(request,"reg.html",{})

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
