#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^$', views.entr_list, name='home'),
    url(r'^entr/(?P<pk>[0-9]+)/$', views.entr_detail, name='entr_detail'),
    url(r'^entr/new/$', views.entr_new, name='ent_new'),
    url(r'^entr/(?P<pk>[0-9]+)/edit/$', views.entr_edit, name='entr_edit'),
]