"""University_Research URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Research.views import home 
from django.views.generic import TemplateView
from Research.views import logins
from Research.views import loginsu
from Research.views import logind
from Research.views import superm
from Research.views import super1
from Research.views import super2
from Research.views import super3
from Research.views import super4
from Research.views import support

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home),
    url(r'^login/',TemplateView.as_view(template_name="login.html"),name="login"),
    url(r'^login1/',TemplateView.as_view(template_name="login1.html"),name="login1"),
    url(r'^logind/',logind),
    url(r'^logins/',logins),
    url(r'^loginsu/',loginsu),
    url(r'^superm/',superm),
    url(r'^super1/',super1),
    url(r'^super2/',super2),
    url(r'^super3/',super3),
    url(r'^super4/',super4),
    url(r'^support/',support),
]
