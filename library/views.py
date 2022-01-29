from django.shortcuts import render,redirect,get_object_or_404
from .models import Books
import mysql.connector 
from operator import itemgetter
from django.contrib import messages 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .forms import BookForm
# Create your views here.
def allbooks(request):
    print("booooookkkkkkkkkkssssssssssssssss")
    context={"books": Books.objects.all()}
    
    return render(request,'book_list.html',context)


def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        adminexist=auth.authenticate(username=email,password=password)
        if adminexist is not None:
            auth.login(request,adminexist)
            return redirect("/dashboard")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

        

def register(request):
    if request.method=='POST':

        fullname=request.POST['fullname']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        
        if fullname=="" or email=="" or password=="" and confirmpassword=="":
            messages.info(request,'Please fill in all the required fields')
            return redirect('register')
        if  User.objects.filter(username=email).exists():
            messages.info(request,'User is already exists')
            return redirect('register')
        if password!=confirmpassword:
            messages.info(request,'Password is not matching')
            return redirect('register')
        adminuser=User.objects.create_user(first_name=fullname,password=password,username=email)
        adminuser.save()
        return redirect('login')

        

    return render(request,'register.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='login')
def book_form(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form=BookForm()
    return render(request,"book_form.html",{'form':form})

@login_required(login_url='login')
def book_update(request,id):
    book = get_object_or_404(Books, pk=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'book_form.html', {'form':form})

@login_required(login_url='login')
def book_delete(request,id):
    book=Books.objects.get(pk=id)
    book.delete()
    return redirect('dashboard')

