from django.shortcuts import render
from .models import bookdetails
from .models import Administrator

# Create your views here.
def home(request):
	return render(request,"home.html")

def about(request):
	return render(request,"about.html")	

def adminsign(request):
    return render(request, "adminsign.html")

def booklistview(request):
    book_list = bookdetails.objects.all()
    return render(request, 'booklist.html',{'book_list':book_list})

