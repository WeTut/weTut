from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from registration.views import register


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'weTut.views.start', name='start'),

    url(r'subscribe', 'weTut.views.subscribe', name='subscribe'),

    #url(r'^register','weTut.views.register',{'backend': 'registration.backends.default.DefaultBackend'},name='register'),
    #url(r'register', register,{'backend': 'registration.backends.default.DefaultBackend'},name='register'),
    url(r'^accounts/', include('registration.urls')),

    url(r'home', 'weTut.views.home', name='home'),
    url(r'questions/', include ('tutorials.urls')),
    url(r'login', 'weTut.views.login_view', name='login'),
    url(r'logout', 'weTut.views.logout_view', name='logout'),
    url(r'profile/', include ('members.urls')),
    # url(r'^weTut/', include('weTut.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)