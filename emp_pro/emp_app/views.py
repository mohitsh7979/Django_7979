from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from emp_app.models import Contact

def home(request):
   return render(request,'home.html',{'emp_name':'mohit'})
def About(request):
   return render(request,'About.html')
   # return HttpResponse('This is about page')
def Course(request):
   return render(request,'Course.html')
   # return HttpResponse('This is course page')
def Fees(request):
   return render(request,'Fees.html')
   # return HttpResponse('This is Fees  page')
def Contact(request):
   if request.method =="get":
      Email=request.GET.get('Email')
      textarea=request.GET.get('textarea')
      Contact=Contact(Email=Email,textarea=textarea,date=datetime.today())
      Contact.save()
      
   return render(request,'Contact.html')
   # return HttpResponse('This is contact page')

# Create your views here.
