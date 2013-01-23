from django import forms
from models import Question, Answer, CommentAnswer
from django.forms import ModelForm

class QuestionForm(ModelForm):
	user = forms.IntegerField(widget=forms.HiddenInput)
	class Meta:
		model = Question
		exclude=['slug']


class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		exclude=['nbLike', 'date', 'user', 'question' ]


class CommentAnswerForm(ModelForm):
	class Meta:
		model = CommentAnswer
		exclude=['answer', 'date', 'user']

