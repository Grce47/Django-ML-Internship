from django.contrib.sessions.models import Session
class AccessRestricter:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.user.is_authenticated:   #When the user logs in
            current_session_key = request.user.logged_in_user.session_key   #the session key of the current user before this login
            if current_session_key and current_session_key != request.session.session_key:  #this session key is different
                #print("CAUGHT SOMETHING",current_session_key,request.session.session_key)
                Session.objects.get(session_key=current_session_key).delete()   #the previous session is force logged out
            request.user.logged_in_user.session_key = request.session.session_key   #this session is now the only session
            request.user.logged_in_user.save()  #and the data is saved to the database

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
