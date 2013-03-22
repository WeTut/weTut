from django.conf.urls import patterns, include, url
from members.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('members.views',		
	url(r'^$', 'members', name='members'), #list of members
	url(r'profile', 'profile', name='profile'), #the profile

	url(r'^(?P<slug>[\w-]+)/?$', 'member', name='member'), #one specific member
)