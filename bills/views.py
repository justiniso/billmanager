from bills.models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response

def list(request):
	bill_list = Bill.objects.all().order_by('-due_date')[:5]
	return render_to_response('list.html', {'bill_list': bill_list})

def create(request):
	if request.method == 'POST':
		form = CreateBillForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/')
	else:
		form = CreateBillForm()

	csrfContext = RequestContext(request, {form: form})
	return render_to_response('create.html', csrfContext)
