# Create your views here.
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response

from members.forms import ProfileForm
from members.models import *

def profile(request):
	profileform = ProfileForm() # An unbound form
	return render_to_response('members/profile.html', {'profileform': profileform}, context_instance=RequestContext(request))
	
