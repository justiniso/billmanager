from django.db import models
from django.contrib.auth.models import User

# TODO: move to a new forms file
# from django.app import forms
from django import forms
from django.forms import ModelForm

import datetime


class Bill(models.Model):
	item = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	due_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	message = models.TextField(max_length=4000, blank=True, null=True)
	recipients = models.ManyToManyField(User, related_name='bill_recipients')

	# Hidden Fields
	creation_date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.item

class CreateBillForm(ModelForm):
	class Meta:
		model = Bill
		fields = ('item', 'amount', 'due_date', 'message')

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)

class UserProfile(models.Model):
	# required
	user = models.OneToOneField(User)

	friends = models.ForeignKey(User, related_name='user_profile_friends')