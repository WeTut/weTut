from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from tutorials.models import Question


class Profile (models.Model):
	email = models.EmailField()
	avatar = models.ImageField(upload_to='members')
	city = models.CharField(max_length = 200)
	state = models.CharField(max_length = 200)
	job = models.CharField(max_length = 200)
	employer = models.CharField(max_length = 200)
	urlPortfolio = models.CharField (max_length = 200)
	urlViadeo = models.CharField (max_length = 200)
	urlLinkedin = models.CharField (max_length = 200)
	urlTwitter = models.CharField (max_length = 200)
	urlFacebook = models.CharField (max_length = 200)
	points = models.IntegerField(default=0)
	status = models.CharField(max_length = 200)
	user = models.ForeignKey(User, unique=True)
	views = models.IntegerField()
	nb_likes = models.IntegerField()
	nb_questions = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.email)

	def user_post_save(sender, instance, created, **kwargs):
    #Create a user profile when a new user account is created
		if created == True:
			Profile.objects.create(user=instance, avatar="members/avatar.jpg", views=0, nb_likes=0, nb_questions=0)
	post_save.connect(user_post_save, sender=User)

	def nbQuestions(self):
		return Question.objects.filter(user=self.user).count()


