# Create your views here.
from movies.models import *
from comments.models import *
from comments.forms import CommentForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def get_or_none(model, **kwargs):
	try:
		return model.objects.get(**kwargs)
	except model.DoesNotExist:
		return None

def home(request):
	movies = Movie.objects.all()
	return render_to_response('movies/home.html',{'movies': movies}, context_instance=RequestContext(request))

def movie_details(request, slug):
	movie = get_or_none(Movie, slug=slug)
	comments = Comment.objects.filter(movie_id=movie.id)
	if request.method == 'POST': # If the form has been submitted...
		form = CommentForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			form.save()
			return HttpResponseRedirect('') # Redirect after POST
	else:
		form = CommentForm(initial={'movie_id': movie.id}) # An unbound form

	return render_to_response('movies/detail.html',locals(), context_instance=RequestContext(request))