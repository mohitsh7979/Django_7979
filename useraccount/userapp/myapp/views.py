from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate



# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("login/")
    return render(request,'login.html')
def login(request):
    if request=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
          login(user)
        
          return redirect('/')

        else:
            return render(request,'login.html')

            
            

        

    # A backend authenticated the credentials
        
    # No backend authenticated the credentials
#  return render(request,'login.html')
def logoutuser(request):
    
    logout(request)
    return redirect("/login")
