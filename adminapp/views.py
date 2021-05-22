from django.shortcuts import render,redirect
from .models import bookdetails
from .models import Administrator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



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


def ad_do_sign_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        result = Administrator.objects.all()
        for x in result:
            if email in x.email:
                if password in x.password:
                    print(x.password)
                    booklist = bookdetails.objects.all()
                    return render(request, 'adminhome.html',{'booklist':booklist})  
                else:
                    return render(request, 'adminsign.html',{'m':'Wrong password'})
            else:
                return render(request, 'adminsign.html',{'m':'Wrong Username'})
    except Exception as e:
        return render(request, 'adminsign.html', {'m': 'An error occured'})

def logoutpage(request):
	return render(request, "home.html")

def addbookview(request):
	return render(request, 'addbook.html')

def addbook(request):
	if request.method == 'POST':
		bookname = request.POST['bookname']
		author = request.POST['author']
		year = request.POST['year']
		publisher = request.POST['publisher']
		pdf = request.FILES['pdf']
		a = bookdetails(bookname=bookname, author=author, year=year, publisher=publisher, 
			 pdf=pdf)
		a.save()
		messages.success(request, 'Book was uploaded successfully')
		return render(request, 'booklistview')
	else:
	    messages.error(request, 'Book was not uploaded successfully')
	    return redirect('addbookview')




