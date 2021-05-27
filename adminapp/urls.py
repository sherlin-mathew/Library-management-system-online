from django.urls import path
from .import views

urlpatterns = [
path('',views.home),
path('about',views.about,name='about'),
path('adminsign',views.adminsign,name='adminsign'),
path('home',views.home,name='home'),
path('booklist',views.booklistview,name='booklist'),
path('ad_do_sign_in',views.ad_do_sign_in),
path('logoutpage',views.logoutpage,name='logoutpage'),
path('addbookview',views.addbookview,name='addbookview'),
path('addbook',views.addbook),
path('managebookview',views.managebookview,name='managebookview'),
path('adminedit/<int:id>', views.adminedit, name='adminedit'),
path('updatebook/<int:id>', views.updatebook, name='updatebook'),
path('deletebook/<int:id>', views.deletebook, name='deletebook'),







]