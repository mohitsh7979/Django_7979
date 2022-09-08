from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect("index")
    # A backend authenticated the credentials
        else:
            return (request,'login.html')
    # No backend authenticated the credentials

    return render(request,'login.html')

def logout_view(request):
    def logout_view(request):
     logout(request)
     return redirect("/login")

