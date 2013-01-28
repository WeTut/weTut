from django import forms
from models import Question, Answer, CommentAnswer
from django.forms import ModelForm

class QuestionForm(ModelForm):
	class Meta:
		model = Question
		exclude=['slug', 'user']


class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		exclude=['nbLike', 'date', 'user', 'question' ]

		widgets = {
		          'answer': forms.Textarea(attrs={'style':"width:100%"}),
        }


class CommentAnswerForm(ModelForm):
	class Meta:
		model = CommentAnswer
		exclude=['answer', 'date', 'user']

