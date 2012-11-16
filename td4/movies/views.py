# Create your views here.
from movies.models import *
from movies.forms import *
from django.shortcuts import render_to_response
from django.db.models.query import QuerySet


def home(request):
	foo = 'Hello'
	return render_to_response('movies/home.html', {'foo': foo})

def movies(request):
	movies = Movie.objects.all()
	return render_to_response('movies/listMovies.html', {'movies': movies })

def movie_details(request, slug):
	movie = Movie.objects.get(slug=slug)
	
	if request.method == 'POST': # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			author = form.cleaned_data['author']
			url = form.cleaned_data['url']
			message = form.cleaned_data['message']
			movie_id = movie.id
			#return HttpResponseRedirect('/thanks/') # Redirect after POST
	else:
		form = CommentForm() # An unbound form

	return render_to_response('movies/movieDetails.html', {'movie': movie, 'form': form })

#context_instance=RequestContext(request)

