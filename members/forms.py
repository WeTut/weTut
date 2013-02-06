from django import forms
from models import Profile
from django.forms import ModelForm

class ProfileForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['avatar'].required = False
	
	class Meta:
		model = Profile
		exclude=['email', 'points', 'status', 'user']

