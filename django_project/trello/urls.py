from django.conf.urls import patterns, url

from trello import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^update_pos$', views.ajax, name='ajax'),
)
