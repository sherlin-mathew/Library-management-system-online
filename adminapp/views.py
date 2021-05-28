from django.shortcuts import render,redirect
from .models import bookdetails
from .models import Administrator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.storage import FileSystemStorage



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
	bookname = request.POST['bookname']
	author = request.POST['author']
	year = request.POST['year']
	publisher = request.POST['publisher']
	pdf = request.FILES['pdf']
    
	a = bookdetails(bookname=bookname, author=author, year=year, publisher=publisher,pdf=pdf)
	a.save()
	return render(request, 'addbook.html',{'m': 'Book was uploaded successfully'})

def managebookview(request):
    book=bookdetails.objects.all()
    return render(request, 'managebook.html', {'book':book})

def adminedit(request,id):
    a=bookdetails.objects.get(id=id)
    return render(request, 'adminedit.html',{'a':a})

def updatebook(request,id):
    bookname = request.POST['bookname']
    author = request.POST['author']
    publisher = request.POST['publisher']
    year = request.POST['year']
    pdf = request.FILES['pdf']
    fs = FileSystemStorage()
    pdf = fs.save(pdf.name,pdf)
    fileurl = fs.url(pdf)
    val=bookdetails(bookname=bookname, author=author, publisher=publisher, year=year, pdf=fileurl)
    val.save()
    return render(request, 'adminedit.html',{'m' : 'Book was Updated Successfully'})

def deletebook(request,id):
    book = bookdetails.objects.get(id=id)
    book.delete()
    return redirect('managebookview')


	

