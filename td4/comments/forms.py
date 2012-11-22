from django import forms
from models import Comment
from django.forms import ModelForm

class CommentForm(ModelForm):
	movie_id = forms.IntegerField(widget=forms.HiddenInput)
	class Meta:
		model = Comment