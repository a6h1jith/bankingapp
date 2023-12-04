from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.

def home(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=user).exists():
                messages.info(request,"username taken")
                return redirect('/register')
            else:
                newuser=User.objects.create_user(username=user, password=password)
                newuser.save()
                return redirect('/login')
        else:
            messages.info(request,"Passwords do not match")
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        user1=request.POST['username']
        password=request.POST['password']
        log=auth.authenticate(username=user1, password=password)
        if log is not None:
            auth.login(request,log)
            return redirect('welcome')
        else:
            messages.info(request,'invalid username or password')
            return redirect('/login')
    return render(request,'login.html')

def welcome(request):
    return render(request, 'welcome.html')

def form(request):
    return render(request,'form.html')

def message(request):
    return render(request,'message.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
