from django.contrib.auth.models import User

"""
Attempts to retrieve user with username. If user does not exist, it will 
create a user with the specified username

"""
def get_or_create_user(username):
	# Check if user exists
	try:
		return User.objects.get(username=username)

	# User does not exist
	except User.DoesNotExist:
		new_user = User.objects.create_user(username=username)
		new_user.save()
		return new_user
