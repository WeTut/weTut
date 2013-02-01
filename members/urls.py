from django.conf.urls import patterns, include, url
from members.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('members.views',
	url(r'^$', 'profile', name='profile'), #list of questions	
)