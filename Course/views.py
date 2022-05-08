from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from videos.models import Video



@login_required
def home(request,index=1):
    context = {
        'videos' : Video.objects.all(),
        'index' : index
    }
    return render(request,'Course/home.html',context=context)