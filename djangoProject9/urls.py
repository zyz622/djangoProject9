"""
URL configuration for djangoProject9 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app01 import views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('datalist/')),
    path('index/', views.index),
    path('user_list/', views.user_list),
    path('user_add/', views.user_add),
    path('lx/', views.lianxi),
    path('login/', views.login),
    path('datalist/', views.GetAll),
    path('info_add/', views.Info_add),
    path('depart/', views.depart),
    path('info_delete/', views.info_delete),

]
