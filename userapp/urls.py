from django.urls import *
from .import views


urlpatterns = [
path('loginview',views.loginview,name='loginview'),
path('sign_in',views.sign_in,name='sign_in'),
path('register',views.register,name='register'),
path('registerview',views.registerview,name='registerview'),
path('otpverify',views.otpverify,name='otpverify'),
path('register_in',views.register_in,name='register_in'),
path('ubooklist',views.ubooklist,name='ubooklist'),
path('logoutpage',views.logoutpage,name='logoutpage'),



]