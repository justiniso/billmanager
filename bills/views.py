from bills.models import *
from bills.forms import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def login(request):
	
	form = LoginForm()
	message = ''

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			# successful authentication
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect('/')

	csrfContext = RequestContext(request, {'form': form, 'message': message})
	return render_to_response('login.html', csrfContext)

def logout(request):
	form = LoginForm()
	message = 'You have successfully logged out'

	auth_logout(request)

	csrfContext = RequestContext(request, {'form': form, 'message': message})
	return render_to_response('login.html', csrfContext)

def register(request):

	errors = {}

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']

		# Check if user exists
		if User.objects.filter(username=username).count():
			errors = {'username': 'User already exists'}

		else:
			new_user = User.objects.create_user(username=username, password=password)
			new_user.first_name = first_name
			new_user.last_name = last_name
			new_user.save()

			# authenticate user
			new_user = authenticate(username=username, password=password)

			if new_user.is_active:
				auth_login(request, new_user)
				# TODO: include some message for new users
				return render_to_response('dashboard.html')

			else:
				errors = {'login': 'Something went wrong'}

	form = RegisterForm()
	csrfContext = RequestContext(request, {'form': form, 'errors': errors})
	return render_to_response('register.html', csrfContext)


@login_required
def dashboard(request):
	bill_list = Bill.objects.filter(creator=request.user).order_by('-due_date')[:20]
	return render_to_response('dashboard.html', {'bill_list': bill_list})

@login_required
def create(request):
	if request.method == 'POST':
		form = CreateBillForm(request.POST)
		if form.is_valid():
			bill = form.save(commit=False)
			bill.creator = request.user
			bill.save()
			return HttpResponseRedirect('/')
	else:
		form = CreateBillForm()

	csrfContext = RequestContext(request, {'form': form})
	return render_to_response('create.html', csrfContext)

def show_bill(request, id):

	# check if bill exists
	try:
		bill = Bill.objects.get(pk=id)
	except:
		raise Http404

	# check if user has access to the bill
	if bill.creator == request.user or bill.recipient == request.user:
		return render_to_response('bill.html', {'bill': bill})

	else:  # user does not have persission to see the bill
		form = LoginForm()
		message = ''
		csrfContext = RequestContext(request, {'form': form, 'message': message})
		return render_to_response('login.html', csrfContext)
	
@login_required
def delete_bill(request, id):

	message = ''

	# check if bill exists
	try:
		bill_to_delete = Bill.objects.get(pk=id)
	except:
		raise Http404

	form = DeleteBillForm(request.POST, instance=bill_to_delete)

	if form.is_valid:  # check csrf
		bill_to_delete.delete()
		return HttpResponseRedirect("/")
	
	else:
		message = 'Unable to delete bill'


	csrfContext = RequestContext(request, {
		'delete_form': form, 
		'bill': bill_to_delete, 
		'message': message})
	return render_to_response('bill.html', csrfContext )



















