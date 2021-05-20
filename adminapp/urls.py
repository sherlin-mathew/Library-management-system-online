from django.urls import path
from .import views

urlpatterns = [
path('',views.home),
path('about',views.about,name='about'),
path('adminsign',views.adminsign,name='adminsign'),
path('home',views.home,name='home'),
path('booklist',views.booklistview,name='booklist'),

]