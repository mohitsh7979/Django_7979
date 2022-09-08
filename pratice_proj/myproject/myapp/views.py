

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login


# Create your views here.
def home(request):
    return render(request,"base.html")

def index(request):
    return render(request,'index.html')

def signuphandle(request):
    if request.method=="POST":
        username=request.POST['usernmae']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['Password']


        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        
        messages.success(request,"sing up successfull")
        return redirect("/index")

def loginhandle(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(email=username,password=password)
        if user is not None:
            login(user)
            return redirect("/index")
        else:
            return redirect('/')

        


        

