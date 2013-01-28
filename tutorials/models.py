from django.db import models
from django.contrib.auth.models import User
from django import forms

class Question (models.Model):
	title = models.CharField(max_length = 200)
	picture = models.ImageField(upload_to='questions')
	message = models.TextField(max_length = 400)
	slug = models.SlugField(max_length = 200)

	user = models.ForeignKey(User)

	def __unicode__(self):
		return u'%s' % (self.title)


class Answer (models.Model):
	nbLike = models.IntegerField()
	answer = models.TextField(default="Entrez votre reponse ici")
	date = models.DateField()

	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)

	def __unicode__(self):
		return u'%s' % (self.date)

	def getComments(self):
		return CommentAnswer.objects.filter(answer=self)
		

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