from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserSignUpForm


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
