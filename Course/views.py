from django.shortcuts import render
import sys
from django.contrib.auth.decorators import login_required

from videos.models import Video
from User.models import pythonCode


@login_required
def home(request,index=1):
    context = {
        'main_video' : Video.objects.all()[index-1],
        'videos' : Video.objects.all(),
        'index' : index,
        'title' : 'Course ' + str(index)
    }
    return render(request,'Course/home.html',context=context)

@login_required
def runcode(request,index=1):
    
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(codeareadata)  #example =>   print("hello world")

            sys.stdout.close()

            sys.stdout = original_stdout  #reset the standard output to its original value

            # finally read output from file and save in output variable

            output = open('file.txt', 'r').read()
            
        except Exception as e:
            # to return error in the code
            sys.stdout = original_stdout
            output = e
    

    context = {
        'main_video' : Video.objects.all()[index-1],
        'videos' : Video.objects.all(),
        'index' : index,
        'title' : 'Course ' + str(index),
        'code' : codeareadata,
        'output' : output
    }

    my_code = pythonCode.create(request.user,codeareadata,output)
    my_code.save()

    return render(request,'Course/home.html',context=context)
