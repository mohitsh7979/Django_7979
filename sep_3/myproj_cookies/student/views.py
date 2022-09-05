from django.shortcuts import render
from urllib import response
from datetime import datetime,timedelta

# Create your views here.
def setcookie(request):
    response=render(request,'student/setcookies.html')
    #response.set_cookie('name','jyoti',max_age=120)     #will alive for 120 sec =2min
    response.set_cookie('name','jyoti',expires=datetime.utcnow()+timedelta(days=3))
    return response

def getcookie(request):
    name=request.COOKIES['name']
    # name=request.COOKIES.get('name')
    # name=request.COOKIES.get('name','xyz')
    return render(request,'student/getcookies.html',{'name':name})

def delcookie(request):
    response=render(request,'student/delcookies.html')
    #response.set_cookie('name','jyoti',max_age=120)     #will alive for 120 sec =2min
    response.delete_cookie('name')
    return response



    
    
   