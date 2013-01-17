from django import forms
from django.contrib.auth.models import User

"""
Field allows the input of a username to query user rather than a
user id.

"""
class UserField(forms.CharField):
	class widget(forms.widgets.TextInput):
		def render(self, name, value, attrs=None):
			if isinstance(value, int):
				value = unicode(User.objects.get(pk=value))
			return super(UserField.widget, self).render(name, value, attrs)

	def clean(self, value):
		value = super(UserField, self).clean(value)
		if not value:
			return None
		try:
			return User.objects.get(username=value)
		except User.DoesNotExist:
			raise forms.ValidationError(u'Invalid username')