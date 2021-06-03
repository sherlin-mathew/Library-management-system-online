
from django.shortcuts import render,redirect
from .models import user
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from adminapp.models import bookdetails
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

def loginview(request):
    return render(request,'login.html')

def sign_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        result = user.objects.all()
        for x in result:
            if email in x.email:
                if password in x.password:
                    return redirect('ubooklist')
                else:
                    return render(request, 'login.html', {'m': 'Incorrect Password'})
            else:
                return render(request, 'login.html', {'m': 'Incorrect Username'})          
    except Exception as e:
        return render(request, 'login.html', {'m': 'An error occured'})

def register(request):
    return render(request, 'register.html')

def random_with_N_digits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start,range_end)

def registerview(request):
    try:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        code = random_with_N_digits(6)
        myresult=user.objects.all()
        f = True
        for x in myresult:
            if email in x.email:
                f = False
        if f:
            val = user(username=username, email=email, password=password, code=code,verified='pending')
            subject = 'Confirmation Mail'
            message = ' Your Confirmation code is '+str(code)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            val.save()
            return render(request, 'verify.html',{'msg':'Request Sent'})
        else:
            return render(request, 'register.html', {'m': 'You entered an existing username.'})
    except Exception as e:
        print(e)
        return render(request, 'register.html', {'m':'An error occured'})

def otpverify(request):
    otp = request.POST['otp']
    codeid = user.objects.last()
    code = codeid.code
    if otp==code:
        codeid.verified = 'verified'
        codeid.save()
        return redirect('ubooklist')
    else:
        return render(request,'verify.html',{'msg':'Entered wrong OTP'})

def register_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        result = user.objects.all()
        for x in result:
            if email in x.email:
                if password in x.password:
                    return redirect('ubooklist')
                else:
                    return render(request, 'login.html', {'m': 'Incorrect Password'})
            else:
                return render(request, 'login.html', {'m': 'Incorrect Username'})          
    except Exception as e:
        return render(request, 'login.html', {'m': 'An error occured'})

def ubooklist(request):
    book = bookdetails.objects.all()
    return render(request, 'ubooklist.html',{'book':book})     

def logoutpage(request):
    return redirect('home') 

def pdfview(request):
    book = bookdetails.objects.all()
    return render(request, 'pdfview.html',{'book':book})     
