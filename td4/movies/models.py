from django.db import models

# Create your models here.
class Director(models.Model):
	slug = models.SlugField(max_length=200)
	name = models.CharField(max_length=200)
	forename = models.TextField()

	def __unicode__(self):
		return u'%s %s' % (self.forename, self.name)

class Country(models.Model):
	slug = models.SlugField(max_length=200)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return u'%s' % (self.name)

class Movie(models.Model):
	slug = models.SlugField(max_length=200)
	title = models.CharField(max_length=200)
	picture = models.CharField(max_length=200)
	year = models.IntegerField()
	synopsis = models.TextField()

	director = models.ForeignKey('Director')
	country = models.ForeignKey('Country')

	def __unicode__(self):
		return u'%s' % (self.title)