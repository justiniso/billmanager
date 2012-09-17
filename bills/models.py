from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

import datetime

# Create your models here.

class Bill(models.Model):
	item = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	due_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	message = models.TextField(max_length=4000, blank=True, null=True)
	recipients = models.ManyToManyField(User, related_name='bill_recipients')

	creation_date = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey(User, related_name='bill_owner')

	def __unicode__(self):
		return self.item

class CreateBillForm(ModelForm):
	class Meta:
		model = Bill
		fields = ('item', 'amount', 'due_date', 'message')

class UserProfile(models.Model):
	# required
	user = models.OneToOneField(User)

	friends = models.ForeignKey(User, related_name='user_profile_friends')