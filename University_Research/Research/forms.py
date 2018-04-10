from django import forms
from Research.models import Scholar
from Research.models import Supervisor
from django.core.validators import MaxValueValidator, MinValueValidator
class LoginS(forms.Form):
  regno=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
  password=forms.CharField(widget=forms.PasswordInput())

  def clean_regno(self):
      regno=self.cleaned_data.get("regno")
      dbn=Scholar.objects.filter(regno=regno)
      if not dbn:
        raise forms.ValidationError("Incorrect Username")
      else:
        return regno
  
  def clean_password(self):
      regno=self.cleaned_data.get("regno")
      password=self.cleaned_data.get("password")
      dbn=Scholar.objects.filter(regno=regno)
      if not dbn:
       raise forms.ValidationError("Incorrect Username")
      else:
       dbm=Scholar.objects.get(regno=regno)
       dbp1=dbm.password
       dbp=(password==dbp1)
       if not dbp:
         raise forms.ValidationError("Incorrect Password")
       else:
         return password

class LoginSu(forms.Form):
  mid=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
  password=forms.CharField(widget=forms.PasswordInput())

  def clean_mid(self):
      mid=self.cleaned_data.get("mid")
      dbn=Supervisor.objects.filter(mid=mid)
      if not dbn:
        raise forms.ValidationError("Incorrect Username")
      else:
        return mid

  def clean_password(self):
      mid=self.cleaned_data.get("mid")
      password=self.cleaned_data.get("password")
      dbn=Supervisor.objects.filter(mid=mid)
      if not dbn:
       raise forms.ValidationError("Incorrect Username")
      else:
       dbm=Supervisor.objects.get(mid=mid)
       dbd=dbm.dean
       if dbd:
         raise forms.ValidationError("Not Eligible")
       else:
        dbp1=dbm.password
        dbp=(password==dbp1)
        if not dbp:
          raise forms.ValidationError("Incorrect Password")
        else:
          return password

class LoginD(forms.Form):
  mid=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
  password=forms.CharField(widget=forms.PasswordInput())

  def clean_mid(self):
      mid=self.cleaned_data.get("mid")
      dbn=Supervisor.objects.filter(mid=mid)
      if not dbn:
        raise forms.ValidationError("Incorrect Username")
      else:
        return mid

  def clean_password(self):
      mid=self.cleaned_data.get("mid")
      password=self.cleaned_data.get("password")
      dbn=Supervisor.objects.filter(mid=mid)
      if not dbn:
       raise forms.ValidationError("Incorrect Username")
      else:
       dbm=Supervisor.objects.get(mid=mid)
       dbp1=dbm.password
       dbd=dbm.dean
       if not dbd:
         raise forms.ValidationError("Not Eligible")
       else:
        dbp=(password==dbp1)
        if not dbp:
          raise forms.ValidationError("Incorrect Password")
        else:
          return password

class editform(forms.Form):
  status=forms.CharField(max_length=10)
  date=forms.DateField()
  remarks=forms.CharField(max_length=500)
  progress=forms.CharField(max_length=30)
  regno=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])

class infof(forms.Form):
  regno=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])

class startform(forms.Form):
  date=forms.DateField()
  message=forms.CharField(max_length=500)
  progress=forms.CharField(max_length=30)
  regno=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])

class regnosearchForm(forms.Form):
  regno=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
 
class namesearchForm(forms.Form):
  regno=forms.CharField(max_length=30)
  
class SunamesearchForm(forms.Form):
  mid=forms.CharField(max_length=30)

class midsearchForm(forms.Form):
  mid=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])

class suregForm(forms.Form):
   name=forms.CharField(max_length=30)
   sex=forms.CharField(max_length=10)
   mid=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   school=forms.CharField(max_length=30)
   email=forms.EmailField()
   aoi=forms.CharField(max_length=500)

class schregForm(forms.Form):
   name=forms.CharField(max_length=30)
   sex=forms.CharField(max_length=10)
   dob=forms.DateField()
   regno=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   school=forms.CharField(max_length=30)
   email=forms.EmailField()
   supervisor=forms.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(000000000)])
   regdate=forms.DateField()
   
   
   
   
 
