from django import forms

class AuthForm(forms.Form):
    username_connexion = forms.CharField(required=True)
    password = forms.CharField(required=True)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea(attrs={'style': "height:75px;"}))
	sender = forms.EmailField()