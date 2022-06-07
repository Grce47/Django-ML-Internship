from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import pythonCode, Orders
import razorpay
from .constants import PaymentStatus
import csv
from django.views.decorators.csrf import csrf_exempt
import json

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            password1=form.cleaned_data.get('password1')
            password2=form.cleaned_data.get('password2')
            if Orders.objects.filter(session_key=request.session.session_key).exists():
                messages.error(request,f'Please Close all Other Open Sessions Or Start a new Session')
                return redirect('User-login')
            else:
                request.session.save()
                print(request.session.session_key)
                order = Orders.objects.create(user=username, first_name=first_name, last_name=last_name,email=email,password1=password1,password2=password2,session_key=request.session.session_key)
                order.save()
    else:
        form = UserSignUpForm()
    
    return render(request, 'User/signup.html', {'form': form, 'title': 'Sign Up','form_isValid': form.is_valid()})


@csrf_exempt
def callback(request):
    session_key=request.session.session_key
    print(session_key)
    order=Orders.objects.get(session_key=session_key)
    user=User.objects.create_user(username=order.user,first_name=order.first_name, last_name=order.last_name, email=order.email, password=order.password1)
    messages.success(request,f'Account created for {order.user}!')
    order.session_key="success"
    order.save()
    return redirect('Course-home')
