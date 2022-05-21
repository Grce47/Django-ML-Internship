from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class pythonCode(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    codearea = models.TextField()
    output = models.TextField()
    session_key = models.TextField(null=True)
    added = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, cur_user,cur_code,cur_output,cur_sessionkey):
        new_code = cls(user=cur_user,codearea=cur_code,output=cur_output,session_key=cur_sessionkey)
        # do something with the book
        return new_code
    
    def __str__(self):
        return self.added.strftime('%Y-%m-%d %H:%M')
    class Meta:
        ordering = ['-added']