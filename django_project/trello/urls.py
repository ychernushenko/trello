from django.conf.urls import patterns, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from trello import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^update_pos$', views.ajax, name='ajax'),
)

if settings.DEBUG:
   urlpatterns += staticfiles_urlpatterns()
