# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response

from members.forms import ProfileForm, FilterForm
from members.models import *

from tutorials.models import Question, FollowQuestion, Answer, CommentAnswer, FollowTag, Tag

def profile(request):
	profile = Profile.objects.get(user=request.user)

	if request.method == 'POST': # If the form has been submitted...
		if request.POST['submit'] == 'profileSubmit':#Si une reponse a ete envoyee
			form = ProfileForm(request.POST, request.FILES) # A form bound to the POST data
			if form.is_valid(): # All validation rules pass
				post = form.save(commit=False)
				if (post.avatar == ''):
					post.avatar = profile.avatar
				post.user = request.user
				post.email = profile.email
				post.points = profile.points
				post.status = profile.status
				post.views = profile.views
				post.nb_likes = profile.nb_likes
				post.nb_questions = profile.nb_questions
				profile.delete()
				post.save()
				profile = Profile.objects.get(user=request.user)
				request.session['profile_user'] = profile

	followedquestions = []
	follows = FollowQuestion.objects.filter(user=request.user) 
	for follow in follows:
		followedquestions.append ( get_object_or_404(Question, id=follow.question.id) )

	if 'deltag' in request.GET:
		idtag = request.GET.get('deltag')
		tag = Tag.objects.filter(id=idtag)
		if tag.exists():
			followTag = FollowTag.objects.filter(tag=tag)
			if followTag.exists():
				FollowTag.objects.get(tag=tag, user=request.user).delete()

	tags = []
	Ftags = FollowTag.objects.all().filter(user=request.user)
	for Ftag in Ftags:
		tags.append(Ftag.tag)

	profileform = ProfileForm(instance=profile) # An unbound form
	
	return render_to_response('members/profile.html', {'profileform': profileform, 'followedquestions':followedquestions, 'tags':tags }, context_instance=RequestContext(request))
	

def members(request):
	membersActifs = Profile.objects.all().order_by('-nb_questions')
	membersPopulaires = Profile.objects.all().order_by('-nb_likes')
	membersVus = Profile.objects.all().order_by('-views')
	membersNotes = Profile.objects.all().order_by('-points')

	return render_to_response('members/members.html', {'membersActifs': membersActifs, 'membersPopulaires': membersPopulaires, 'membersVus': membersVus, 'membersNotes': membersNotes}, context_instance=RequestContext(request))

def member(request,slug):
	profile = get_object_or_404(User, username=slug)
	member = get_object_or_404(Profile, user=profile)
	questions = Question.objects.all().filter(user_id=profile).filter(validate=0)
	answers = Answer.objects.all().filter(user_id=profile)
	comments = CommentAnswer.objects.all().filter(user_id=profile)
	tutorials = Question.objects.all().filter(user_id=profile).filter(validate=1)
	followedquestions = FollowQuestion.objects.all().filter(user_id=profile)

	if slug != request.user.username:
		views = member.views + 1
		Mid = member.id
		Profile.objects.filter(id=Mid).update(views=views)

	if 'deltag' in request.GET:
		idtag = request.GET.get('deltag')
		tag = Tag.objects.filter(id=idtag)
		if tag.exists():
			followTag = FollowTag.objects.filter(tag=tag)
			if followTag.exists():
				FollowTag.objects.get(tag=tag, user=request)

	tags = []
	Ftags = FollowTag.objects.all().filter(user=profile)
	for Ftag in Ftags:
		tags.append(Ftag.tag)

	return render_to_response('members/member.html', {'profile': profile, 'member': member, 'questions':questions, 'answers':answers, 'comments':comments, 'tutorials':tutorials, 'tags':tags, 'followedquestions':followedquestions}, context_instance=RequestContext(request))