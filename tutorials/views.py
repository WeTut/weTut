# Create your views here.
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response
from datetime import datetime 

from tutorials.forms import QuestionForm, AnswerForm, CommentAnswerForm, FilterForm
from tutorials.models import *

def questions(request):

	filterform = FilterForm()
	if request.is_ajax() and request.method == 'POST':
		questions = Question.objects.all().order_by(request.POST['filter'])
		
	else :
		questions = Question.objects.all()
		print('date')

	return render_to_response('tutorials/questions.html', {'questions': questions, 'filterform':filterform}, context_instance=RequestContext(request))

def question(request,slug):
	question = get_object_or_404(Question, slug=slug)
	question.views += 1
	question.save()
	answers = Answer.objects.filter(question=question)

	if request.method == 'POST': # If the form has been submitted...
		if request.user.is_authenticated():# If there isn't any logged user
			
			if request.POST['submit'] == 'answerSubmit':#Si une reponse a ete envoyee 
				form = AnswerForm(request.POST, request.FILES) # A form bound to the POST data
				if form.is_valid(): # All validation rules pass
					post = form.save(commit=False)
					post.date = datetime.now()
					post.user = request.user
					post.question = question
					post.currentUserLiked = False
					post.save()

			elif request.POST['submit'] == 'commentSubmit':#Si un commentaire a ete envoye
				form = CommentAnswerForm(request.POST, request.FILES) # A form bound to the POST data
				if form.is_valid(): # All validation rules pass
					post = form.save(commit=False)
					post.date = datetime.now()
					post.user = request.user
					post.answer = get_object_or_404(Answer, id=request.POST['answerId'])
					post.save()

			elif request.POST['submit'] == 'likeSubmit':#Si un like a ete envoye
				like = Like()
				like.user = request.user
				like.answer = get_object_or_404(Answer, id=request.POST['answerId'])
				alreadyLiked = like.hasLiked()
				if not alreadyLiked:
					like.save()					
					return HttpResponse('OK')
				else:
					return HttpResponse('error')


	for answer in answers:
		like = Like.objects.filter(answer=answer, user=request.user)
		if like.exists():
			answer.currentUserLiked = True

	answerform = AnswerForm() # An unbound form
	commentform = CommentAnswerForm() # An unbound form

	return render_to_response('tutorials/question.html', {'question': question, 'answerform':answerform, 'commentform':commentform, 'answers':answers}, context_instance=RequestContext(request))


def ask(request):
	if request.method == 'POST': # If the form has been submitted...
		form = QuestionForm(request.POST, request.FILES) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			post = form.save(commit=False)
			title = form.cleaned_data['title']
			post.user = request.user
			post.slug = str(slugify(title))
			post.views = 0
			post.date = datetime.now()
			post.save()
			return HttpResponseRedirect('/questions') # Redirect after POST
	else:
		form = QuestionForm() # An unbound form #initial={'user': request.user}

	return render_to_response('tutorials/ask.html', {'form': form}, context_instance=RequestContext(request))
