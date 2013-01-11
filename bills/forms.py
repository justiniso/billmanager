# TODO: move to a new forms file
# from django.app import forms
from django import forms
from django.forms import ModelForm
from bills.models import *

class CreateBillForm(ModelForm):
	class Meta:
		model = Bill
		fields = ('item', 'amount', 'due_date', 'message')
		exlude = ('creator', )

class DeleteBillForm(forms.ModelForm):
	class Meta:
		model = Bill
		fields = []

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)
	first_name = forms.CharField(max_length=24)
	last_name = forms.CharField(max_length=24)