from django.conf.urls import patterns, url

urlpatterns = patterns('polls.views',
    url(r'^contact_polls/$', 'contact'),
    url(r'^essai_00/$', 'essai_00'),
    url(r'^menus_polls/$', 'menus_polls'),
)
