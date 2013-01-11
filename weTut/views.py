# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from weTut.forms import AuthForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def start(request):
	return render_to_response('general/start.html', context_instance=RequestContext(request))

def home(request):
	return render_to_response('general/home.html', context_instance=RequestContext(request))

def login_view(request):
	if request.method == 'POST': # If the form has been submitted...
		form = AuthForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/home/') # Redirect after POST

		else:
			form = AuthForm() # An unbound form

			return render(request, 'layout/login.html', {
		        'form': form,
		    })

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/home/')
	