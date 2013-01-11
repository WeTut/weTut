from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
	email = models.EmailField()
	#pictureProfile = models.ImageField()
	city = models.CharField(max_length = 200)
	state = models.CharField(max_length = 200)
	urlPortfolio = models.CharField (max_length = 200)
	urlViadeo = models.CharField (max_length = 200)
	urlLinkedin = models.CharField (max_length = 200)
	urlTwitter = models.CharField (max_length = 200)
	urlFacebook = models.CharField (max_length = 200)
	points = models.IntegerField()
	status = models.CharField(max_length = 200)

	def __unicode__(self):
		return u'%s' % (self.email)

class Answer (models.Model):
	nbLike = models.IntegerField()
	text = models.TextField()
	date = models.DateField()

	user = models.ForeignKey(User)

	def __unicode__(self):
		return u'%s' % (self.date)


class Question (models.Model):
	title = models.CharField(max_length = 200)
	picture = models.ImageField(upload_to = "{{ STATIC_URL }}images/testImages/")
	message = models.CharField(max_length = 400)


	user = models.ForeignKey(User)

	def __unicode__(self):
		return u'%s' % (self.title)

class Software(models.Model):
	name = models.CharField(max_length = 200)

	def __unicode__(self):
		return u'%s' % (self.name)


class Tags(models.Model):
	name = models.CharField(max_length = 200)

	def __unicode__(self):
		return u'%s' % (self.name)

class Media(models.Model):
	link = models.CharField(max_length = 200)

	question = models.ForeignKey("Question")

	def __unicode__(self):
		return u'%s' % (self.link)