from django import forms
from models import Question
from django.forms import ModelForm

class QuestionForm(ModelForm):
	class Meta:
		model = Question