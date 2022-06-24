from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import pythonCode, Order
import razorpay
from .constants import PaymentStatus
import csv
from django.views.decorators.csrf import csrf_exempt
import json

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            session_key=request.session.session_key
            username=form.cleaned_data.get('username')
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            password1=form.cleaned_data.get('password1')
            password2=form.cleaned_data.get('password2')
            if Order.objects.filter(session_key=request.session.session_key).exists() or Order.objects.filter(user=username).exists():
                messages.error(request,f'Please Close all Other Open Sessions Or Start a new Session')
                return redirect('User-login')
            else:
                order = Order.objects.create(
                user=username, first_name=first_name, last_name=last_name,
                email=email,password1=password1,password2=password2,session_key=session_key
                    )
                order.date_joined=str(order.date)
                order.save()
    else:
        form = UserSignUpForm()
    
    return render(request, 'User/signup.html', {'form': form, 'title': 'Sign Up','form_isValid': form.is_valid()})


@csrf_exempt
def callback(request):
    session_key=request.session.session_key
    payment_id=request.GET['payment_id']
    client=razorpay.Client(auth=("rzp_live_SN60y2d5pTIgRT","S6ATAbXIVkO0vb41z9VLAcj3"))
    temp=client.payment.fetch(payment_id)
    order=Order.objects.get(session_key=session_key)
    user=User.objects.create_user(username=order.user,first_name=order.first_name, last_name=order.last_name, email=order.email, password=order.password1)
    messages.success(request,f'Account created for {order.user}!')
    order.session_key="success"
    order.method=temp['method']
    order.save()
    return redirect('Course-home')


@login_required
def download_data(request):
    if request.user.is_staff:
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['User','Session Key', 'first_name', 'last_name','Date','date_joined','method'])
        for code in Order.objects.all():
            column = [code.user,code.session_key,code.first_name,code.last_name,code.date , code.date_joined,code.method]
            writer.writerow(column)
        
        response['Content-Disposition'] = 'attachment; filename="codes.csv"'
        return response
    else:
        return redirect('Course-home')
