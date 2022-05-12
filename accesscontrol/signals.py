from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from accesscontrol.models import LoggedInUser
from django.contrib.sessions.models import Session

@receiver(user_logged_in)
def on_user_logged_in(sender, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))     #the user is (maybe) added to the list of logged-in users

@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    request = kwargs.get('request')     #the request will be used to find the session data
    if request.user.is_authenticated:
        Session.objects.filter(session_key=request.session.session_key).delete()    #the current session is deleted
        try:
            Session.objects.get(session_key=request.user.logged_in_user.session_key)    #trying to find the 1st session
            try:
                Session.objects.get(session_key=request.user.logged_in_user.session_key_2)  #trying to find the 2nd session
            except Session.DoesNotExist:    #if the 2nd session is not found (which means we deleted it in line 13)
                print("2nd instance logged out")    #these print statements are for debugging purposes, but they will be removed later when all the bugs are fixed
                request.user.logged_in_user.session_key_2 = None
                request.user.logged_in_user.save()  #saved with 2nd key nulled
        except Session.DoesNotExist:
            print("1st instance logged out")    #if the 1st session is not found (line 13 again)
            if request.user.logged_in_user.session_key_2:   #in case the second session exists, that will take over as the 1st session
                request.user.logged_in_user.session_key = request.user.logged_in_user.session_key_2
                request.user.logged_in_user.session_key_2 = None
                request.user.logged_in_user.save()
            else:
                request.user.logged_in_user.delete()    #if not, then the user is no longer logged in
            
