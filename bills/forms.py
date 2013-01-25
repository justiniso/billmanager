
from django import forms
from django.forms import ModelForm
from bills.models import *
from bills.form_fields import *

class CreateBillForm(ModelForm):
	recipient = forms.EmailField(max_length=100)
	class Meta:
		model = Bill
		fields = ('item', 'amount', 'due_date', 'message')
		exclude = ('creator', )

	def clean(self, *args, **kwargs):
		return super(CreateBillForm, self).clean(*args, **kwargs)

class DeleteBillForm(forms.ModelForm):
	class Meta:
		model = Bill
		fields = []

class MarkBillForm(forms.ModelForm):
	class Meta:
		model = Bill
		fields = []

class LoginForm(forms.Form):
	username = forms.EmailField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)

class RegisterForm(forms.Form):
	username = forms.EmailField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)
	first_name = forms.CharField(max_length=24)
	last_name = forms.CharField(max_length=24)