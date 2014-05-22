from django.conf.urls import patterns, url

from mapApp import views



urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^about/$', views.about, name='about'),
	url(r'^sponsors/$', views.sponsors, name='sponsors'),
	
)