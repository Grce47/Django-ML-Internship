from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from accesscontrol.models import LoggedInUser
@receiver(user_logged_in)
def on_user_logged_in(sender, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))     #the user is (maybe) added to the list of logged-in users

@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    usr = LoggedInUser.objects.filter(user=kwargs.get('user')).delete()   #the user is deleted from the list of logged-in users