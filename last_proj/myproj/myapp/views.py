
from email import message
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


# Create your views here.
# def index(request):
#     return render(request,'base.html')
def home(request):
    return render(request,'myapp/home.html')

def about(request):
    return render(request,'myapp/about.html')
    # return HttpResponse('This is about page')
def course(request):
    return render(request,'myapp/course.html')
    # return HttpResponse('This is course page  ')
def contact(request):
     return render(request,'myapp/contact.html')
    # # return HttpResponse('This is contact page')

def signuphandle(request):
    if request.method=="POST":
        Username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['Conformpassword']

        if len(Username) >10:
            messages.error(request,"username must be under 10 character")
            return redirect('/')
        if not Username.isalnum():
            messages.error(request,"username should only contain latters and number")
        if password != password2:
            messages.error(request,"password do not match")


        myuser=User.objects.create_user(Username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        
        messages.success(request,"you account has been create succefull")
        return redirect('/')


    else:
        return HttpResponse('404 page not found')



def loginhandle(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        mypass=request.POST['pass']
        user = authenticate(username=loginusername, password=mypass)
        if user is not None:
            login(request,user)
            return redirect("/about")
    # A backend authenticated the credentials
        else:
            return redirect("/contact")
    # No backend authenticated the credentials

def logouthandle(request):
       logout(request)
       messages.success(request,"successfull Logout !!!!")
       return redirect("/course")


