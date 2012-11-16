from django.db import models
from django import forms

class Comment(models.Model):
	author = models.CharField(max_length=200)
	mail = models.EmailField()
	url = models.CharField(max_length=200)
	content = models.TextField()
	movie_id = models.IntegerField()
	#movie = models.ForeignKey('movies.Movie')

	def __unicode__(self):
		return u'%s' % (self.author)