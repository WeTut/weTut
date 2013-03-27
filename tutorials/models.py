from django.db import models
from django.contrib.auth.models import User
from django import forms
from stdimage import StdImageField
from django.contrib.admin.widgets import AdminDateWidget 


class Tag(models.Model):
	name = models.CharField(max_length = 200)
	type = models.IntegerField()

	def __unicode__(self):
		return u'%s' % (self.name)


class Question (models.Model):
	
	title = models.CharField(max_length = 200)
	picture = StdImageField(upload_to='questions', blank=True, size=(310, 224, True), thumbnail_size=(155, 120, True))
	message = models.TextField(max_length = 400)
	slug = models.SlugField(max_length = 200)
	views = models.IntegerField()
	answers = models.IntegerField()
	user = models.ForeignKey(User)
	tag1 = models.IntegerField()
	tag2 = models.IntegerField()
	tag3 = models.IntegerField()
	date = models.DateField()
	validate = models.BooleanField(default=False)

	media1 = StdImageField(upload_to='questions/medias_supplementaires', blank=True, size=(800, 600, True), thumbnail_size=(80, 80, True))
	media2 = StdImageField(upload_to='questions/medias_supplementaires', blank=True, size=(800, 600, True), thumbnail_size=(80, 80, True))
	media3 = StdImageField(upload_to='questions/medias_supplementaires', blank=True, size=(800, 600, True), thumbnail_size=(80, 80, True))

	video = models.CharField(max_length = 200)

	currentUserFollows = False
	currentUserLikes = False
	
	def __unicode__(self):
		return u'%s' % (self.title)

	def getAnswersCount(self):
		return Answer.objects.filter(question=self).count()

	def getLikesCount(self):
		return LikeTuto.objects.filter(tutorial_id=self).count()


class Answer (models.Model):
	answer = models.TextField()
	date = models.DateField()

	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	nb_likes = models.IntegerField()
	usefull = models.BooleanField(default=False)

	currentUserLiked = False
	currentUserDisliked = False

	def __unicode__(self):
		return u'%s' % (self.date)

	def getComments(self):
		return CommentAnswer.objects.filter(answer=self)

	def getLikesCount(self):
		likes = LikeAnswer.objects.filter(answer=self, type=1).count()
		dislikes = LikeAnswer.objects.filter(answer=self, type=0).count()
		return max(likes-dislikes, 0)


class Software(models.Model):
	name = models.CharField(max_length = 200)

	def __unicode__(self):
		return u'%s' % (self.name)

class Media(models.Model):
	#link = models.CharField(max_length = 200)
	link = StdImageField(upload_to='media', blank=True, size=(310, 224, True), thumbnail_size=(160, 120, True))
	question = models.ForeignKey("Question")

	def __unicode__(self):
		return u'%s' % (self.link)

class CommentAnswer(models.Model):
	user = models.ForeignKey(User)
	comment = models.TextField(default="Entrez votre commentaire ici")
	date = models.DateField()
	answer = models.ForeignKey(Answer)

class LikeAnswer(models.Model):
	user = models.ForeignKey(User)
	answer = models.ForeignKey(Answer)
	type = models.IntegerField()

class LikeTuto(models.Model):
	user = models.ForeignKey(User)
	tutorial = models.ForeignKey(Question)

class ActualityTag(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	tag = models.ForeignKey(Tag)
	date = models.DateField()

class ActualityQuestion(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	answer = models.ForeignKey(Answer)
	date = models.DateField()

class FollowQuestion (models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)

class FollowTag (models.Model):
	user = models.ForeignKey(User)
	tag = models.ForeignKey(Tag)