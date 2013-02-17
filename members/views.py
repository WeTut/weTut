# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response

from members.forms import ProfileForm
from members.models import *

from tutorials.models import Question, FollowQuestion

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
				post.points = 0
				post.status = profile.status
				profile.delete()
				post.save()
				profile = Profile.objects.get(user=request.user)

	followedquestions = []
	follows = FollowQuestion.objects.filter(user=request.user) 
	for follow in follows:
		followedquestions.append ( get_object_or_404(Question, id=follow.question.id) )

	profileform = ProfileForm(instance=profile) # An unbound form
	
	return render_to_response('members/profile.html', {'profileform': profileform, 'followedquestions':followedquestions }, context_instance=RequestContext(request))
	
