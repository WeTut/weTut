from django import forms
from models import Question, Answer, CommentAnswer
from django.forms import ModelForm

class QuestionForm(ModelForm):
	class Meta:
		model = Question
		exclude=['slug', 'user', 'views']

class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		exclude=['currentUserLiked', 'date', 'user', 'question' ]

		widgets = {
		          'answer': forms.Textarea(attrs={'style':"width:100%"}),
        }

class CommentAnswerForm(ModelForm):
	class Meta:
		model = CommentAnswer
		exclude=['answer', 'date', 'user']
		widgets = {
		          'comment': forms.Textarea(attrs={'style':"width:100%"}),
        }

class FilterForm(forms.Form):
    FILTER_CHOICES = (
        ('date', 'Date'),
        ('-views', 'Nombre de vues'),
    )    
    
    filter = forms.ChoiceField(choices=FILTER_CHOICES, widget=forms.Select())
