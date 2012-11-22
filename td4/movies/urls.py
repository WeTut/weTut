from django.conf.urls import patterns, include, url
from movies.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('movies.views',
	url(r'^$', 'home', name='home'),
	url(r'^(?P<slug>[\w-]+)/?$', 'movie_details', name='movie_details'),
    # Examples:
    # url(r'^$', 'td4.views.home', name='home'),
    # url(r'^td4/', include('td4.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)