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
			
	questions = Question.objects.all().order_by('-date')
 
	if request.user.is_authenticated() :
		if request.method == 'POST' : 
			if request.POST['submit'] == 'followSubmit':
				if request.POST['hidden'] == 'follow':
					follow = FollowQuestion()
					follow.user = request.user
					follow.question = get_object_or_404(Question, id=request.POST['questionId'])
					follow.save()
					return HttpResponse('saved')
				elif request.POST['hidden'] == 'unfollow':
					follow = get_object_or_404(FollowQuestion, question=request.POST['questionId'], user=request.user)
					follow.delete()
					return HttpResponse('deleted')			
			elif request.POST['submit'] == 'filterSubmit': 
				questions = Question.objects.all().order_by(request.POST['filter'])	

		for question in questions:
			question.currentUserFollows = False
			follow = FollowQuestion.objects.filter(question=question, user=request.user)
			if follow.exists():
				question.currentUserFollows = True

	return render_to_response('tutorials/questions.html', {'questions': questions, 'filterform':filterform}, context_instance=RequestContext(request))

def tutorials(request):

	filterform = FilterForm()
	if request.is_ajax() and request.method == 'POST':
		tutorials = Question.objects.all().order_by(request.POST['filter'])
		
	else :
		tutorials = Question.objects.all().order_by('-date')

	return render_to_response('tutorials/tutorials.html', {'tutorials': tutorials, 'filterform':filterform}, context_instance=RequestContext(request))

def question(request,slug):
	question = get_object_or_404(Question, slug=slug)
	question.views += 1
	question.save()
	answers = Answer.objects.filter(question=question).order_by('-nb_likes')

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
					post.nb_likes = 0
					post.save()
					question.answers += 1
					question.save()


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
				like.save()
				
				answer = get_object_or_404(Answer, id=request.POST['answerId'])
				answer.nb_likes +=1
				answer.save()
				return HttpResponse( like.answer.getLikesCount() )

			elif request.POST['submit'] == 'validateSubmit':#Valider une question
				usefull_checked = request.POST.getlist('usefull') #Get the list of the checked answers
				Answer.objects.filter(id__in=usefull_checked).update(usefull=True) #According to this list, Set the matching "usefull" field to True
				question.validate=True #The Question is finished. Set Bool validate attribute to True
				question.save() #Save it
				return HttpResponseRedirect('/tutoriels') # Redirect

			for answer in answers:
				answer.currentUserLiked = False
				like = Like.objects.filter(answer=answer, user=request.user)
				if like.exists():
					answer.currentUserLiked = True


	answerform = AnswerForm() # An unbound form
	commentform = CommentAnswerForm() # An unbound form

	return render_to_response('tutorials/question.html', {'question': question, 'answerform':answerform, 'commentform':commentform, 'answers':answers}, context_instance=RequestContext(request))

def tutorial(request,slug):
	tutorial = get_object_or_404(Question, slug=slug)
	answers = Answer.objects.filter(question=tutorial).order_by('-nb_likes')

	return render_to_response('tutorials/tutorial.html', {'question': tutorial, 'answers':answers}, context_instance=RequestContext(request))

def ask(request):
	technicaltags = Tag.objects.filter(type=0)
	softwaretags = Tag.objects.filter(type=1)

	if request.method == 'POST': # If the form has been submitted...
		form = QuestionForm(request.POST, request.FILES) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			post = form.save(commit=False)
			title = form.cleaned_data['title']
			post.user = request.user
			post.slug = str(slugify(title))
			post.views = 0
			post.answers = 0
			post.date = datetime.now()

			tech1 = request.POST['technical1']
			soft1 = request.POST['software1']
			tech2 = request.POST['technical2']
			soft2 = request.POST['software2']
			tech3 = request.POST['technical3']
			soft3 = request.POST['software3']

			post.tag1 = max(tech1, soft1)
			post.tag2 = max(tech2, soft2)
			post.tag3 = max(tech3, soft3)

			post.save()
			return HttpResponseRedirect('/questions') # Redirect after POST
	else:
		form = QuestionForm() # An unbound form #initial={'user': request.user}

	return render_to_response('tutorials/ask.html', {'form': form, 'technicaltags':technicaltags, 'softwaretags':softwaretags}, context_instance=RequestContext(request))
