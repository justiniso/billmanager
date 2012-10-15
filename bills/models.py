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
	recipient = models.ManyToManyField(User, related_name='bill_recipient')

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

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)
	first_name = forms.CharField(max_length=24)
	last_name = forms.CharField(max_length=24)

class UserProfile(models.Model):
	# required
	user = models.OneToOneField(User)

	friends = models.ManyToManyField(User, related_name='friends')

class Friendship(models.Model):
	from_friend = models.ForeignKey(User, related_name='friend_set')
	to_friend = models.ForeignKey(User, related_name='to_friend_set')

	def __unicode__(self):
		return u'%s, %s' % (
			self.from_friend.email,
			self.to_friend.email)

	class Meta:
		unique_together = (('to_friend', 'from_friend'),)