from django import forms

class AuthForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)