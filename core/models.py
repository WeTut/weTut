from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
	email = models.EmailField()
	avatar = models.ImageField(upload_to='questions')
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