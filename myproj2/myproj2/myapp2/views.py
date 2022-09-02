from django.shortcuts import render
from django.http import HttpResponse 
from myapp2.forms import ProfileForm
from myapp2.models import Profile

def SaveProfile(request):
    saved=False


    if request.method=='POST':
        MyProfileForm=ProfileForm(request.POST,request.FILES)
        if MyProfileForm.is_valid():
            profile=Profile()
            profile.name=MyProfileForm.cleaned_data["name"]
            profile.picture=MyProfileForm.cleaned_data["picture"]
            profile.save()
            saved=True
            
    else:
        MyProfileForm=ProfileForm()

    print(locals())

    return render(request,'saved.html',locals())

def profile_create(request):
    return render(request,'profile.html')
