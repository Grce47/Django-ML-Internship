from django.db import models
from django.conf import settings
# Create your models here.
class LoggedInUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user',on_delete=models.CASCADE)   #the user whose data is stored
    session_key = models.CharField(max_length=32,blank=True,null=True)  #the 1st session (older)
    session_key_2 = models.CharField(max_length=32,blank=True,null=True)    #the 2nd session (newer)
    def __str__(self):
        self.user.username