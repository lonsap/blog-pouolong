from django.conf.urls import patterns, url, include
from . import views  # N'oubliez pas d'importer les vues
#-----------------------
from django.views.generic import TemplateView  # L'import a changé, attention !
from .models import Post
from django.views.generic import ListView

#-----------------------

urlpatterns = [
    url(r'^new_blog/$', ListView.as_view(model=Post,)),
    url(r'^voir_contacts/$', views.voir_contacts, name='voir_contacts'),
#    url(r'^new_blog/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
#-----------------------
    url(r'^faq/$', TemplateView.as_view(template_name='blog/faq.html')),
#    url(r'^categorie/(?P<slug>.+)$', views.voir_categorie),
#-----------------------
]
