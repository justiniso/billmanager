from bills.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect('/')
			else:
				return render_to_response('login.html')
		else:
			return render_to_response('login.html')
	else:
		form = LoginForm()

	csrfContext = RequestContext(request, {'form': form})
	return render_to_response('login.html', csrfContext)


def dashboard(request):
	bill_list = Bill.objects.all().order_by('-due_date')[:5]
	return render_to_response('dashboard.html', {'bill_list': bill_list})

@login_required
def create(request):
	if request.method == 'POST':
		form = CreateBillForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = CreateBillForm()

	csrfContext = RequestContext(request, {'form': form})
	return render_to_response('create.html', csrfContext)
