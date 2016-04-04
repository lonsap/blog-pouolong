#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('blog.views',
    url(r'^index/$', 'post_list'),
#    url(r'^accueil_blog/$', 'post_list'),
#    url(r'^date_blog/$', 'date_actuelle'),
#    url(r'^couleurs/$', 'couleurs'),
#    url(r'^illustration/$', 'maquette'),
#    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
#    url(r'^contact_blog/$', 'contact_blog'),
#   url(r'^contact_blog/$', views, name='contact'),
)
