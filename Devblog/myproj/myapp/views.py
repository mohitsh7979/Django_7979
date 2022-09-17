
from django.shortcuts import render,redirect
from myapp.models import signup
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# Create your views here.
def front(request):
    return render(request,'front.html')

def signuphandle(request):
   if request.method=="POST":
    name=request.POST['username']
    f_name=request.POST['fname']
    l_name=request.POST['lname']
    e_mail=request.POST['email']
    p_assword=request.POST['password']
    conform_password=request.POST['conformpassword']

    myuser=signup(username=name,fname=f_name,lname=l_name,password=p_assword,conformpassword=conform_password,email=e_mail)
    myuser.save()
    # myuser=User.objects.create_user(name,p_assword)
    # myuser.first_name=f_name
    # myuser.last_name=l_name
    # myuser.save()


def loginhandle(request):
   if request.method=="POST":
    name=request.POST['username']
    p_assword=request.POST['password']
    user=authenticate(request,username=name,password=p_assword)
    if user is  None:
        login(request,user)
        return redirect("/texteditor")
    else:
        return redirect("/signup")

def logouthandle(request):
    logout(request)

    # messages.success(request,"successfull Logout !!!!")
    return redirect("/")
def text(request):
    return render(request,'texteditor.html')