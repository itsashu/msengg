"""MedNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import patterns, include, url
# from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from webMS.settings import *
# saveRadiologistInfo
urlpatterns = patterns('web.views',
    url(r'^index/(?P<some_data>[\w-]+)/$', 'index', name = 'index'),
    url(r'^home', 'home', name = 'home'),
    url(r'^catalog', 'catalog', name = 'catalog'),
    url(r'^$', 'home', name = 'home'), 
   )

urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': STATIC_ROOT}
))