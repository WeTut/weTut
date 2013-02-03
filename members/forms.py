from django import forms
from models import Profile
from django.forms import ModelForm

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		exclude=['email', 'points', 'status','user']