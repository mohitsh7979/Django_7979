from django.shortcuts import render

def home(request):
    return render(request,"home.html",{'name':"Mohit"})
def add(request):
    var1=int(request.POST['num1'])
    var2=int(request.POST['num2'])
    ans=var1+var2
    
    return render(request,'result.html',{'result':ans})

# Create your views here.
