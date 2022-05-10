from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from accesscontrol.models import LoggedInUser
from django.contrib.sessions.models import Session
@receiver(user_logged_in)
def on_user_logged_in(sender, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))     #the user is (maybe) added to the list of logged-in users

@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    usr = LoggedInUser.objects.get(user=kwargs.get('user'))  #the user is found from the list of logged-in users
    request = kwargs.get('request')
    Session.objects.filter(session_key=request.session.session_key).delete()
    try:
        Session.objects.get(session_key=usr.session_key)
        try:
            Session.objects.get(session_key=usr.session_key_2)
        except Session.DoesNotExist:
            print("2nd instance logged out")
            request.user.logged_in_user.session_key_2 = None
            request.user.logged_in_user.save()
    except Session.DoesNotExist:
        print("1st instance logged out")
        request.user.logged_in_user.delete()
