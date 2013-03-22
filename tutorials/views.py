# Create your views here.
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response
from datetime import datetime 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from tutorials.forms import QuestionForm, AnswerForm, CommentAnswerForm, FilterForm
from tutorials.models import *

from members.models import Profile

def questions(request):
	
	if 'filterQuestion' not in request.session:
		request.session['filterQuestion'] = '-date'

	filterform = FilterForm()
	currentag = 0	
	tags = Tag.objects.all()
	userfollowstag = False

	questions_list = Question.objects.filter(validate=False).order_by(request.session['filterQuestion'])	
 
	if request.method == 'POST' and 'submit' in request.POST:

		if request.user.is_authenticated() : 
			
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

			elif request.POST['submit'] == 'followTagSubmit':
				if request.POST['hidden'] == 'follow':
					follow = FollowTag()
					follow.user = request.user
					follow.tag = get_object_or_404(Tag, id=request.POST['tagId'])
					follow.save()
					return HttpResponse('saved')
				elif request.POST['hidden'] == 'unfollow':
					follow = get_object_or_404(FollowTag, tag=request.POST['tagId'], user=request.user)
					follow.delete()
					return HttpResponse('deleted')

		if request.POST['submit'] == 'filterSubmit': 
			questions_list = Question.objects.filter(validate=False).order_by(request.POST['filter'])
			request.session['filterQuestion'] = request.POST['filter']


	paginator = Paginator(questions_list, 10)
	questions = paginator.page(1)
	if 'page' in request.GET:
		page = request.GET.get('page')
		try:
			questions = paginator.page(page)
		except PageNotAnInteger:
			questions = paginator.page(1)
		except EmptyPage:
			questions = paginator.page(paginator.num_pages)

	if 'tag' in request.GET:
		currentag = int(request.GET['tag'])

		if request.user.is_authenticated() :
			followTag = FollowTag.objects.filter(tag=currentag, user=request.user)
			if followTag.exists():
				userfollowstag = True

		temp = []
		for question in questions:
			if question.tag1 == currentag or question.tag2 == currentag or question.tag3 == currentag:
				temp.append(question)
		questions = temp


	if request.user.is_authenticated() :
		for question in questions:
			question.currentUserFollows = False
			follow = FollowQuestion.objects.filter(question=question, user=request.user)
			if follow.exists():
				question.currentUserFollows = True	

	return render_to_response('tutorials/questions.html', {'questions': questions, 'filterform':filterform, 'tags':tags, 'currentag':currentag, 'userfollowstag':userfollowstag, 'filtervalue':request.session['filterQuestion'] }, context_instance=RequestContext(request))

def tutorials(request):

	filterform = FilterForm()

	if 'filterTuto' not in request.session:
		request.session['filterTuto'] = '-date'

	tutorials_list = Question.objects.filter(validate=True).order_by(request.session['filterTuto'])
	print ("REQUEST.POST ",request.POST)
	if request.method == 'POST' and 'submit' in request.POST:


		if request.POST['submit'] == 'filterSubmit':
			print ("FILTER")
			tutorials_list = Question.objects.filter(validate=True).order_by(request.POST['filter'])
			request.session['filterTuto'] = request.POST['filter']

		elif request.POST['submit'] == 'likeTutoSubmit':
			print ("LIKE")
			if request.POST['hidden'] == 'like':
				like = LikeTuto()
				like.user = request.user
				like.tutorial = get_object_or_404(Question, id=request.POST['tutoId'])
				like.save()
				return HttpResponse('liked')
			elif request.POST['hidden'] == 'dislike':
				like = get_object_or_404(LikeTuto, tutorial=request.POST['tutoId'], user=request.user)
				like.delete()
				return HttpResponse('disliked')


	paginator = Paginator(tutorials_list, 10)
	tutorials = paginator.page(1)
	if 'page' in request.GET:
		page = request.GET.get('page')
		try:
			tutorials = paginator.page(page)
		except PageNotAnInteger:
			tutorials = paginator.page(1)
		except EmptyPage:
			tutorials = paginator.page(paginator.num_pages)

	if request.user.is_authenticated() :
		for tutorial in tutorials:
			tutorial.currentUserLikes = False
			like = LikeTuto.objects.filter(tutorial=tutorial, user=request.user)
			if like.exists():
				tutorial.currentUserLikes = True

	return render_to_response('tutorials/tutorials.html', {'tutorials': tutorials, 'filterform':filterform, 'filtervalue':request.session['filterTuto'] }, context_instance=RequestContext(request))
	

def question(request,slug):
	question = get_object_or_404(Question, slug=slug)
	question.views += 1
	question.save()

	answers = Answer.objects.filter(question=question).order_by('-nb_likes')
	ready = False

	if request.user.is_authenticated():

		actualityTag = ActualityTag()
		try:
			actualityTag = ActualityTag.objects.get(user=request.user, question=question)
		except actualityTag.DoesNotExist:
			actualityTag = None

		if actualityTag is not None:
			actualityTag.delete()


		actualityQuestion = ActualityQuestion()
		try:
			actualityQuestion = ActualityQuestion.objects.get(user=request.user, question=question)
		except actualityQuestion.DoesNotExist:
			actualityQuestion = None

		if actualityQuestion is not None:
			actualityQuestion.delete()


		for answer in answers:
			answer.currentUserLiked = False
			answer.currentUserDisliked = False
			like = LikeAnswer.objects.filter(answer=answer, user=request.user)
			if like.exists():				
				like = LikeAnswer.objects.get(answer=answer, user=request.user)
				if like.type == 0:
					answer.currentUserDisliked = True
				else:
					answer.currentUserLiked = True


		if  request.method == 'POST': # If the form has been submitted...

			if 'answersubmit' in request.POST:#Si une reponse a ete envoyee 
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

					#create actuality for all who follow this question
					followers = FollowQuestion.objects.filter(question=question)
					for follower in followers:
						if request.user != follower.user:
							actuality = ActualityQuestion()
							actuality.user = follower.user
							actuality.answer = post
							actuality.question = question
							actuality.date = datetime.now()
							actuality.save()


			elif 'commentsubmit' in request.POST:#Si un commentaire a ete envoye
				form = CommentAnswerForm(request.POST, request.FILES) # A form bound to the POST data
				if form.is_valid(): # All validation rules pass
					post = form.save(commit=False)
					post.date = datetime.now()
					post.user = request.user
					post.answer = get_object_or_404(Answer, id=request.POST['answerId'])
					post.save()

			elif 'submit' in request.POST:#Si un like a ete envoye
				answer = get_object_or_404(Answer, id=request.POST['answerId'])
				currentlike = LikeAnswer.objects.filter(answer=answer, user=request.user)
				if currentlike.exists():
					currentlike = LikeAnswer.objects.get(answer=answer, user=request.user)
				else:
					currentlike = LikeAnswer()
					currentlike.user = request.user
					currentlike.answer = answer				

				if request.POST['submit'] == 'likesubmit':
					currentlike.type = 1
				else:
					currentlike.type = 0

				currentlike.save()
				answer.nb_likes = answer.getLikesCount()
				answer.save()

				return HttpResponse( answer.nb_likes )


			elif 'validatesubmit' in request.POST:#Valider une question
				usefull_checked = request.POST.getlist('usefull') #Get the list of the checked answers
				Answer.objects.filter(id__in=usefull_checked).update(usefull=True) #According to this list, Set the matching "usefull" field to True
				question.validate=True #The Question is finished. Set Bool validate attribute to True
				question.save() #Save it
				return HttpResponseRedirect('/tutoriels') # Redirect

		if  request.method == 'GET' and 'ready' in request.GET :
			ready = True


	answerform = AnswerForm() # An unbound form
	commentform = CommentAnswerForm() # An unbound form

	return render_to_response('tutorials/question.html', {'question': question, 'answerform':answerform, 'commentform':commentform, 'answers':answers, 'ready':ready}, context_instance=RequestContext(request))

def tutorial(request,slug):
	tutorial = get_object_or_404(Question, slug=slug)
	answers = Answer.objects.filter(question=tutorial).order_by('-nb_likes')

	return render_to_response('tutorials/tutorial.html', {'question': tutorial, 'answers':answers}, context_instance=RequestContext(request))

def ask(request):
	technicaltags = Tag.objects.filter(type=0)
	softwaretags = Tag.objects.filter(type=1)

	if request.method == 'POST': # If the form has been submitted...
		form = QuestionForm(request.POST, request.FILES) # A form bound to the POST data
		#formMedia = MediaForm(request.POST, request.FILES)
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

			profile = get_object_or_404(Profile, user=request.user)
			profile.nb_questions += 1
			profile.save()

			#media = formMedia.save(commit=False)
			#media.question_id = post.id

			#create actuality for all who follow one of these tags
			followers = FollowTag.objects.filter(tag__in=[post.tag1, post.tag2, post.tag3])
			for follower in followers:
				if request.user != follower.user:
					actuality = ActualityTag()
					actuality.user = follower.user
					actuality.tag = follower.tag
					actuality.question = post
					actuality.date = datetime.now()
					actuality.save()

			return HttpResponseRedirect('/questions') # Redirect after POST
	else:
		form = QuestionForm() # An unbound form #initial={'user': request.user}

	return render_to_response('tutorials/ask.html', {'form': form, 'technicaltags':technicaltags, 'softwaretags':softwaretags}, context_instance=RequestContext(request))
