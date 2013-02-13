from django.db import models
from django.contrib.auth.models import User
from django import forms
from stdimage import StdImageField

class Question (models.Model):
	title = models.CharField(max_length = 200)
	#picture = models.ImageField(upload_to='questions')
	picture = StdImageField(upload_to='questions', blank=True, size=(440, 380), thumbnail_size=(160, 120, True))
	message = models.TextField(max_length = 400)
	slug = models.SlugField(max_length = 200)
	views = models.IntegerField()
	answers = models.IntegerField()
	user = models.ForeignKey(User)
	date = models.DateField()

	def __unicode__(self):
		return u'%s' % (self.title)

	def getAnswersCount(self):
		return Answer.objects.filter(question=self).count()


class Answer (models.Model):
	currentUserLiked = models.BooleanField(default=1)
	answer = models.TextField(default="Entrez votre reponse ici")
	date = models.DateField()

	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	nb_likes = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.date)

	def getComments(self):
		return CommentAnswer.objects.filter(answer=self)

	def getLikesCount(self):
		return Like.objects.filter(answer=self).count()


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

class CommentAnswer(models.Model):
	user = models.ForeignKey(User)
	comment = models.TextField(default="Entrez votre commentaire ici")
	date = models.DateField()
	answer = models.ForeignKey(Answer)

class Like(models.Model):
	user = models.ForeignKey(User)
	answer = models.ForeignKey(Answer)

	def hasLiked(self):
		return Like.objects.filter(user=self.user, answer=self.answer)