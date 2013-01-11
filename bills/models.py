from django.db import models
from django.contrib.auth.models import User
import datetime


class Bill(models.Model):
	creator = models.ForeignKey(User)
	item = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	due_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	message = models.TextField(max_length=4000, blank=True, null=True)
	recipient = models.ManyToManyField(User, related_name='bill_recipient')

	# Hidden Fields
	creation_date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.item



class UserProfile(models.Model):
	# required
	user = models.OneToOneField(User, unique=True)

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