from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'weTut.views.start', name='start'),

    url(r'home', 'weTut.views.home', name='home'),
    url(r'questions', 'weTut.views.questions', name='questions'),
    url(r'question', 'weTut.views.question', name='question'),
    url(r'login', 'weTut.views.login_view', name='login'),
    url(r'logout', 'weTut.views.logout_view', name='logout'),
    # url(r'^weTut/', include('weTut.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()