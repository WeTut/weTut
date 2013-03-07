from django import forms
from models import Profile
from django.forms import ModelForm

class ProfileForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['avatar'].required = False
		self.fields['city'].required = False
		self.fields['state'].required = False
		self.fields['job'].required = False
		self.fields['employer'].required = False
		self.fields['urlPortfolio'].required = False
		self.fields['urlViadeo'].required = False
		self.fields['urlLinkedin'].required = False		
		self.fields['urlTwitter'].required = False
		self.fields['urlFacebook'].required = False
	
	class Meta:
		model = Profile
		exclude=['email', 'points', 'status', 'user', 'views', 'nb_questions', 'nb_likes']


class FilterForm(forms.Form):
    FILTER_CHOICES = (
        ('-nb_likes', 'Popularite'),
        ('-points', 'Points'),
        ('-nb_questions', 'Nombre de questions'),
        ('-views', 'Nombre de vues'),
    )    
    
    filtermembers = forms.ChoiceField(choices=FILTER_CHOICES, widget=forms.Select())

