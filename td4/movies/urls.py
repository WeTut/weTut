from django.conf.urls import patterns, include, url
from movies.views import *

urlpatterns = patterns('movies.views',
    url(r'^$', movies, name='movies'),
    url(r'^(?P<slug>[\w-]+)/$', movie_details, name='movie_details')
)