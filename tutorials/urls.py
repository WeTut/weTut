from django.conf.urls import patterns, include, url
from tutorials.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('tutorials.views',
url(r'^$', 'questions', name='questions'), #list of questions
url(r'ask', 'ask', name='ask'), #ask a question

url(r'^(?P<slug>[\w-]+)/?$', 'question', name='question'), #one specific question
)