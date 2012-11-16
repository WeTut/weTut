from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin
from movies.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'td4.views.home', name='home'),
    # url(r'^td4/', include('td4.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

	#url(r'', home, name='home'),
    (r'^movies/', include('movies.urls')),
)

urlpatterns += staticfiles_urlpatterns()