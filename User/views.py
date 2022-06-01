from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required
from .models import pythonCode, Order
import razorpay
from .constants import PaymentStatus
import csv
from django.views.decorators.csrf import csrf_exempt
import json


def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        # amount = 100
        # client = razorpay.Client(
        #             auth=("rzp_test_Txuj1dmhZX8vUs", "6wb44PRbVVFXWvCKWPMgfMDC"))
        # payment = client.order.create({'amount': amount, 'currency': 'INR',
        #                                'payment_capture': '1'})
        # if(payment):
        #     print("hsdkjsakjhfsakdlhfskdajlfhsakdjfhakdsjfhkdsaljfhaksljfdhsakjf")
        
        # payment = client.order.create({'amount': amount, 'currency': 'INR',
        #                                'payment_capture': '1'})
        if form.is_valid():
            user=form.save()
            amount=1
            client = razorpay.Client(
                    auth=("rzp_test_Txuj1dmhZX8vUs", "6wb44PRbVVFXWvCKWPMgfMDC"))
            razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
                    )
            order = Order.objects.create(
            user=user, amount=amount, provider_order_id=razorpay_order["id"]
                )
            order.save()
            return render(
            request,
            "User/payment.html",
            {
                "callback_url": "http://" "172.105.54.200" + "/callback/",
                "razorpay_key": "rzp_test_Txuj1dmhZX8vUs",
                "order": order,
            },
        )
        

            # form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request,f'Account created for {username}!')
            # if request.user.is_authenticated:   
            #     return redirect('Course-home')
            # return redirect('User-login')
    else:
        form = UserSignUpForm()
    
    return render(request, 'User/signup.html', {'form': form, 'title': 'Sign Up','form_isValid': form.is_valid()})

@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=("rzp_test_Txuj1dmhZX8vUs", "6wb44PRbVVFXWvCKWPMgfMDC"))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            messages.success(request,f'Account created for {order.user}!')
            return redirect('Course-home')
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            u=order.user
            u.delete()
            messages.error(request,f'Payment Not Recieved!')
            return redirect('User-login')
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        u=order.user
        u.delete()
        messages.error(request,f'Payment Error!')
        return redirect('User-login')
