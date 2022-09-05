from django.shortcuts import render
from django.http import HttpResponse 
from.functions.functions import handle_uploaded_file
from myapp1.forms import studentForms
def index(request):
    if request.method=='POST':
        student =studentForms(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("file uploaded successfuly")
    else:
        student=studentForms()
        return render(request,"index.html",{'form':student})

