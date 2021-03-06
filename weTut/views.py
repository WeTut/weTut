# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from weTut.forms import AuthForm
from weTut.forms import ContactForm
from registration.forms import RegistrationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.core.mail import send_mail

import re

from tutorials.models import *
from tutorials.forms import QuestionForm, AnswerForm, CommentAnswerForm, FilterForm

from registration.backends import get_backend
from members.models import Profile

def start(request):
	questionsDate = Question.objects.filter(validate=0).order_by('-id')[:3]
	questionsViews = Question.objects.filter(validate=0).order_by('-views')[:3]
	tutorialsDate = Question.objects.filter(validate=1).order_by('-id')[:3]
	tutorialsLike = Question.objects.filter(validate=1).order_by('-liketuto')[:3]

	return render_to_response('general/start.html', {'questionsDate': questionsDate, 'questionsViews': questionsViews, 'tutorialsDate':tutorialsDate, 'tutorialsLike':tutorialsLike}, context_instance=RequestContext(request))

def home(request):
	questionsDate = Question.objects.filter(validate=0).order_by('-id')[:3]
	questionsViews = Question.objects.filter(validate=0).order_by('-views')[:3]
	tutorialsDate = Question.objects.filter(validate=1).order_by('-id')[:3]
	tutorialsLike = Question.objects.filter(validate=1).order_by('-liketuto')[:3]
	membersPopulaires = Profile.objects.order_by('-nb_likes')[:4]
	if request.user.is_authenticated():
		actualityQuestion = ActualityQuestion.objects.filter(user=request.user).order_by('-date')[:3]
		actualityTag = ActualityTag.objects.filter(user=request.user).order_by('-date')[:3]
		return render_to_response('general/home.html', {'questionsDate': questionsDate, 'questionsViews': questionsViews, 'tutorialsDate':tutorialsDate, 'tutorialsLike':tutorialsLike, 'actualityQuestion':actualityQuestion, 'actualityTag':actualityTag, 'membersPopulaires':membersPopulaires}, context_instance=RequestContext(request))
	else:
		return render_to_response('general/home.html', {'questionsDate': questionsDate, 'questionsViews': questionsViews, 'tutorialsDate':tutorialsDate, 'tutorialsLike':tutorialsLike, 'membersPopulaires':membersPopulaires}, context_instance=RequestContext(request))

def login_view(request):
	if request.method == 'POST': # If the form has been submitted...
		form = AuthForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			username = request.POST['username_connexion']
			password = request.POST['password']
			if re.match("[^@]+@[^@]+\.[^@]+", username):
				username = User.objects.get(email=username)

			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					request.session['profile_user'] = user.get_profile()
					return HttpResponseRedirect('/') # Redirect after POST

		else:
			form = AuthForm() # An unbound form

			#return render(request, 'layout/login.html', {
		    #    'form': form,
		    #})
	else :
		return HttpResponseRedirect('/facebook/login/')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def subscribe(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			return HttpResponseRedirect('/')
	else:
		form = RegistrationForm()
	return render(request, 'general/signup.html',{'form': RegistrationForm()})

def guide(request):
	return render(request,'general/guide.html')

def legal(request):
	return render(request,'general/legal.html')

def contact(request):
	if request.method == 'POST': # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			subject=form.cleaned_data['subject']
			message=form.cleaned_data['message']
			email=form.cleaned_data['sender']
			recipients=['teamwetut@gmail.com']
			#Send the mail
			send_mail(subject, message, email, recipients)
			return HttpResponseRedirect('/thanks/') # Redirect after POST
	else:
		form = ContactForm() # An unbound form

	return render(request, 'general/contact.html', {'form': form})

def thanks(request):
	return render(request,'general/thanks.html')
