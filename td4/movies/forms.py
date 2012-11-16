from django import forms


class CommentForm(forms.Form):
	author = forms.CharField()
	mail = forms.EmailField()
	url = forms.URLField(required=False)
	message = forms.CharField(widget=forms.Textarea())
	movie_id = forms.IntegerField(widget=forms.HiddenInput())