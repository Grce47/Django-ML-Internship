from django.db import models
from django.conf import settings
# Create your models here.
class LoggedInUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user',on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32,blank=True,null=True)
    def __str__(self):
        self.user.username