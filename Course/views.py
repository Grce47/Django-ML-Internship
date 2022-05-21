import traceback
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
        with open('user_code.py','w') as f:
            f.writelines(codeareadata)
        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(open('user_code.py').read())
            sys.stdout.close()

            sys.stdout = original_stdout  #reset the standard output to its original value

            # finally read output from file and save in output variable

            output = open('file.txt', 'r').read()
            
        except Exception as e:
            # to return error in the code
            e_type,e_val,e_tb = sys.exc_info()
            sys.stdout = original_stdout
            with open('file.txt','a') as fh:
                traceback.print_exception(e_type,e_val,e_tb,file=fh)
            output = open('file.txt', 'r').read()
    

    context = {
        'main_video' : Video.objects.all()[index-1],
        'videos' : Video.objects.all(),
        'index' : index,
        'title' : 'Course ' + str(index),
        'code' : codeareadata,
        'output' : output
    }
    if(not codeareadata.isspace() and len(codeareadata)):
        print(len(codeareadata))
        my_code = pythonCode.create(request.user,codeareadata,output,request.session.session_key)
        my_code.save()
    return render(request,'Course/home.html',context=context)
