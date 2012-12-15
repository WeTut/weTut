# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

def start(request):
	return render_to_response('general/start.html', context_instance=RequestContext(request))

def home(request):
	return render_to_response('general/home.html', context_instance=RequestContext(request))

def questions(request):
	return render_to_response('general/questions.html', context_instance=RequestContext(request))

def question(request):
	return render_to_response('general/question.html', context_instance=RequestContext(request))