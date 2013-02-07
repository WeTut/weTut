# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from weTut.forms import AuthForm
from registration.forms import RegistrationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.contrib.auth.models import User
import re

from registration.backends import get_backend


def start(request):
	return render_to_response('general/start.html', context_instance=RequestContext(request))

def home(request):
	return render_to_response('general/home.html', context_instance=RequestContext(request))

def login_view(request):
	if request.method == 'POST': # If the form has been submitted...
		form = AuthForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			username = request.POST['username']
			password = request.POST['password']
			if re.match("[^@]+@[^@]+\.[^@]+", username):
				username = User.objects.get(email=username)

			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/home/') # Redirect after POST

		else:
			form = AuthForm() # An unbound form

			#return render(request, 'layout/login.html', {
		    #    'form': form,
		    #})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/home/')

def subscribe(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			return HttpResponseRedirect('/')
	else:
		form = RegistrationForm()
	return render(request, 'general/signup.html',{'form': RegistrationForm()})

# def register(request, backend, success_url='/', form_class=None,
#              disallowed_url='registration_disallowed',
#              template_name='general/signup.html',
#              extra_context=None):
#     """
#     Allow a new user to register an account.

#     The actual registration of the account will be delegated to the
#     backend specified by the ``backend`` keyword argument (see below);
#     it will be used as follows:

#     1. The backend's ``registration_allowed()`` method will be called,
#        passing the ``HttpRequest``, to determine whether registration
#        of an account is to be allowed; if not, a redirect is issued to
#        the view corresponding to the named URL pattern
#        ``registration_disallowed``. To override this, see the list of
#        optional arguments for this view (below).

#     2. The form to use for account registration will be obtained by
#        calling the backend's ``get_form_class()`` method, passing the
#        ``HttpRequest``. To override this, see the list of optional
#        arguments for this view (below).

#     3. If valid, the form's ``cleaned_data`` will be passed (as
#        keyword arguments, and along with the ``HttpRequest``) to the
#        backend's ``register()`` method, which should return the new
#        ``User`` object.

#     4. Upon successful registration, the backend's
#        ``post_registration_redirect()`` method will be called, passing
#        the ``HttpRequest`` and the new ``User``, to determine the URL
#        to redirect the user to. To override this, see the list of
#        optional arguments for this view (below).
    
#     **Required arguments**
    
#     None.
    
#     **Optional arguments**

#     ``backend``
#         The dotted Python import path to the backend class to use.

#     ``disallowed_url``
#         URL to redirect to if registration is not permitted for the
#         current ``HttpRequest``. Must be a value which can legally be
#         passed to ``django.shortcuts.redirect``. If not supplied, this
#         will be whatever URL corresponds to the named URL pattern
#         ``registration_disallowed``.
    
#     ``form_class``
#         The form class to use for registration. If not supplied, this
#         will be retrieved from the registration backend.
    
#     ``extra_context``
#         A dictionary of variables to add to the template context. Any
#         callable object in this dictionary will be called to produce
#         the end result which appears in the context.

#     ``success_url``
#         URL to redirect to after successful registration. Must be a
#         value which can legally be passed to
#         ``django.shortcuts.redirect``. If not supplied, this will be
#         retrieved from the registration backend.
    
#     ``template_name``
#         A custom template to use. If not supplied, this will default
#         to ``registration/registration_form.html``.
    
#     **Context:**
    
#     ``form``
#         The registration form.
    
#     Any extra variables supplied in the ``extra_context`` argument
#     (see above).
    
#     **Template:**
    
#     registration/registration_form.html or ``template_name`` keyword
#     argument.
    
#     """
#     backend = get_backend(backend)
#     if not backend.registration_allowed(request):
#         return redirect(disallowed_url)
#     if form_class is None:
#         form_class = backend.get_form_class(request)

#     if request.method == 'POST':
#         form = form_class(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             new_user = backend.register(request, **form.cleaned_data)
#             if success_url is None:
#                 to, args, kwargs = backend.post_registration_redirect(request, new_user)
#                 return redirect(to, *args, **kwargs)
#             else:
#                 return redirect(success_url)
#     else:
#         form = form_class()
    
#     if extra_context is None:
#         extra_context = {}
#     context = RequestContext(request)
#     for key, value in extra_context.items():
#         context[key] = callable(value) and value() or value

#     return render_to_response(template_name,
#                               {'form': form},
#                               context_instance=context)	