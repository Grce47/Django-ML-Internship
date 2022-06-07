from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus


# Create your models here.

class pythonCode(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    codearea = models.TextField()
    output = models.TextField()
    session_key = models.TextField(null=True)
    username = models.TextField(null=True)
    added = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, cur_user,cur_code,cur_output,cur_sessionkey,cur_username):
        new_code = cls(user=cur_user,codearea=cur_code,output=cur_output,session_key=cur_sessionkey,username=cur_username)
        return new_code
    
    def __str__(self):
        return self.added.strftime('%Y-%m-%d %H:%M')
    class Meta:
        ordering = ['-added']
class Orders(models.Model):
    user = models.CharField(max_length=150,default="temp")
    session_key=models.CharField(max_length=150,default="temp",null=False)
    first_name = models.CharField(max_length=150,default="temp")
    last_name = models.CharField(max_length=150,default="temp")
    email = models.EmailField(max_length=150,default="temp@temp.com")
    # username = models.CharField(max_length=150,default="temp")
    password1=models.CharField(max_length=150,default="temp")
    password2=models.CharField(max_length=150,default="temp")
    def __str__(self):
        return f"{self.id}-{self.user}"