from django.shortcuts import render,redirect
from .models import user
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
#from adminapp.models import *
#from random import randint
#from django.core.mail import send_mail
from django.conf import settings

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
