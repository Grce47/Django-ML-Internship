from django.contrib.sessions.models import Session
class AccessRestricter:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.user.is_authenticated:   #When the user logs in

            current_session_key = request.user.logged_in_user.session_key  
            current_session_key_2 = request.user.logged_in_user.session_key_2   #the session keys of the current user before this login

            if current_session_key_2 and current_session_key != request.session.session_key and current_session_key_2 != request.session.session_key:  #this session key is different
                print("CAUGHT SOMETHING",current_session_key,current_session_key_2,request.session.session_key)  #debug codes
                Session.objects.get(session_key=current_session_key).delete()   #the 1st session is force logged out
                request.user.logged_in_user.session_key = request.user.logged_in_user.session_key_2   #the 2nd session is now the 1st session
                request.user.logged_in_user.session_key_2 = request.session.session_key   #this session is now the 2nd session
            if not current_session_key:     #in case of 1st login
                print("1st Login",current_session_key,current_session_key_2,request.session.session_key)
                request.user.logged_in_user.session_key = request.session.session_key
            elif not current_session_key_2 and current_session_key != request.session.session_key:    #in case of 2nd login
                print("2nd Login",current_session_key,current_session_key_2,request.session.session_key)
                request.user.logged_in_user.session_key_2 = request.session.session_key
            request.user.logged_in_user.save()                  #and the data is saved to the database
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        
        return response
