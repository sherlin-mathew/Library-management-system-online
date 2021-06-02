from django.urls import path
from . import views


urlpatterns = [
path('loginview',views.loginview,name='loginview'),
path('sign_in',views.sign_in,name='sign_in'),
path('register',views.register,name='register'),

]