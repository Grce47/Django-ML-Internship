from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required
from .models import pythonCode

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            if request.user.is_authenticated:
                return redirect('Course-home')
            return redirect('User-login')
    else:
        form = UserSignUpForm()
    
    return render(request, 'User/signup.html', {'form': form, 'title': 'Sign Up'})

@login_required
def listcodes(request):
    context = {
        'title' : 'Submissions of ' + str(request.user.username),
        'codes' : pythonCode.objects.filter(user=request.user)
    }
    return render(request,'User/list_codes.html',context=context)


@login_required
def detailcodes(request,index=1):
    code = pythonCode.objects.filter(user=request.user)[index-1]
    
    context = {
        'title' : str(code),
        'code'  : code
    }
    return render(request,'User/detail_code.html',context)