"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EMSapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('k/',views.idt),
    path('mn/',views.dy),
    path('kl',views.btp,name="hm"),
    path('ab/',views.about,name="abt"),
    path('cnt/',views.contact,name="ct"),
    path('reg/',views.register,name="rg"),
    path('ind/',views.index,name="indx"),
    path('log/',views.loginofemp,name="login"),
    path('work/',views.workdo,name="wd"),
    path('emp/<int:w>/',views.empupdate,name="emup"),
    path('emdt/<int:y>/',views.empdelete,name="emd"),
    path('',views.home,name="hm"),
]

