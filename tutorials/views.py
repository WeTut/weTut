# Create your views here.
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response

from tutorials.forms import QuestionForm
from tutorials.models import *

def questions(request):
	questions = Question.objects.all()
	return render_to_response('tutorials/questions.html', {'questions': questions}, context_instance=RequestContext(request))

def question(request,slug):
	question = get_object_or_404(Question, slug=slug)
	return render_to_response('tutorials/question.html', {'question': question}, context_instance=RequestContext(request))

def ask(request):
	if request.method == 'POST': # If the form has been submitted...
		form = QuestionForm(request.POST, request.FILES) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			post = form.save(commit=False)
			title = form.cleaned_data['title']
			post.slug = str(slugify(title))
			post.save()
			return HttpResponseRedirect('/questions') # Redirect after POST
	else:
		form = QuestionForm() # An unbound form

	return render_to_response('tutorials/ask.html', {'form': form}, context_instance=RequestContext(request))