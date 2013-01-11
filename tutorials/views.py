# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from tutorials.forms import QuestionForm
from tutorials.models import *



def questions(request):
	questions = Question.objects.all()
	return render_to_response('tutorials/questions.html', {'questions': questions }, context_instance=RequestContext(request))

def question(request):
	return render_to_response('tutorials/question.html', context_instance=RequestContext(request))

def ask(request):
	if request.method == 'POST': # If the form has been submitted...
		form = QuestionForm(request.POST, request.FILES) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			form.save()
			return HttpResponseRedirect('') # Redirect after POST
	else:
		form = QuestionForm() # An unbound form

	return render_to_response('tutorials/ask.html', {'form': form}, context_instance=RequestContext(request))