from django import forms
from models import Question, Answer
from django.forms import ModelForm

class QuestionForm(ModelForm):
	class Meta:
		model = Question
		exclude=['slug']


class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		exclude=['nbLike', 'date', 'user', 'question' ]
