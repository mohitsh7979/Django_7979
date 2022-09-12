from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from myapp.models import shoping
from myapp.forms import shopingform

# Create your views here.
def index(request):
    return render(request,'home.html')
def home(request):
    return render(request,'home.html')

def men(request):
    return render(request,'men.html')

def women(request):
    return render(request,'women.html')

def kids(request):
    return render(request,'kids.html')

def electronics(request):
    return render(request,'elctronics.html')

def signuphandle(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']
        Conformpassword=request.POST['Conformpassword']

        if len(username) >10:
            messages.error(request,"username must be under 10 character")
            return redirect('/')
        if not username.isalnum():
            messages.error(request,"username should only contain latters and number")
        if password != Conformpassword:
            messages.error(request,"password do not match")



        myuser=shoping(name=username,password=password,first_name=fname,last_name=lname)
        myuser.save()
        messages.success(request,"you account has been create succefull")
        return redirect("/men")
    else:
        return HttpResponse('404 page not found')

def loginhandle(request):
    if request.method == 'POST':
        username = request.POST['loginusername']
        password = request.POST['pass']
        user = authenticate(request, name=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/kids")
        else:
            
            return redirect("/about")
        

def logouthandle(request):
    logout(request)
    messages.success(request,"successfull Logout !!!!")
    return redirect("/home")



def abc(request):
    return render(request,'abc.html')

