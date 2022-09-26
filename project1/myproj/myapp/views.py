from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from myapp.models import shoping
from myapp.forms import shopingform
from django.contrib.auth.backends import BaseBackend
from myapp.models import *
from math import ceil



# Create your views here.
def index(request):
    return render(request,'home.html')
def new(request):
    products=product.objects.all()
    context={'products': products}
    print(products)
    return render(request,'new.html',context)

def buynow(request):
    if request.method=="POST":
        items_json= request.POST['itemsJson']
        name=request.POST['name']
        email=request.POST['email']
        state=request.POST['state']
        city=request.POST['city']
        address=request.POST['address']+" "+request.POST['address2']
        zip=request.POST['zip']

        myuser=order(name=name,email=email,state=state,city=city,address=address,zip_code=zip, items_json= items_json)
        messages.success(request,"succeffull")
        myuser.save()
        thank=True
        return render(request,'buynow.html',{'thank':thank})

        
    return render(request,'buynow.html')
def add(request):
    return render(request,'addtocart.html')

def addtocart(request):
    if request.method=="POST":  
      user=request.user
      product_id=request.POST['prod_id']
    #   kproduct=request.POST['prod_id']
      wproduct=womenproduct.objects.get(id=product_id)
    #   mproduct=menproduct.objects.get(id=product_id)
    #   kproduct=kidsproduct.objects.get(id=product_id)
      cart(user=user,wproduct=wproduct).save()
      
      return redirect("/cart")
def addtokcart(request):
    if request.method=="POST":  
      user=request.user
      product_id=request.POST['prod_id']
      kproduct=kidsproduct.objects.get(id=product_id)
      kcart(user=user,kproduct=kproduct).save()
      
      return redirect("/cart")

def addtomcart(request):
    if request.method=="POST":  
      user=request.user
      product_id_k=request.POST['prod_id_k']
      print(product_id_k)
      mproduct=menproduct.objects.get(id=product_id_k)
      print(mproduct)
      mcart(user=user,mproduct=mproduct).save()
      
      return redirect("/cart")


def showcart(request):
    user=request.user
    mcat=cart.objects.filter(user=user)
    kcat=kcart.objects.filter(user=user)
    mencart=mcart.objects.filter(user=user)
    amount=0.0
    newamount=0.0
    menamount=0.0
    shipping_amount=70.0
    a=0.0
    x=0.0
    y=0.0
    c=0.0
    total_amount=0.0
    cart_product=[p for p in cart.objects.all() if p.user==user ]
    kcart_product=[p for p in kcart.objects.all() if p.user==user]
    men_cart_product=[p for p in mcart.objects.all() if p.user==user]
    # cart_product.extend(kcart_product)
    # print(cart_product)
    # print(kcart_product)
    # print(men_cart_product)
    if cart_product and kcart_product and men_cart_product:
        for p in cart_product:
              tempamount=(p.wproduct.price )
              amount+=tempamount
              total_amount=amount+shipping_amount
        
        for j in kcart_product:
             total=(j.kproduct.price)
             newamount+=total
             a=newamount+shipping_amount

        for k in men_cart_product:
             mentotal=(k.mproduct.price)
             menamount+=mentotal
             c=menamount+shipping_amount
     
        print(amount+newamount+menamount)
        print(a+total_amount+c)
         
        x=amount+newamount+menamount
        y=a+total_amount+c
        
    return render(request,'addtocart.html',{'carts':mcat,'kcarts':kcat,'total_amount':y,'amount':x,'mcarts':mencart})



    
def men(request):
    products=menproduct.objects.all()
    context={'products': products}
    print(products)
    return render(request,'men.html',context)

def abc(request,id):
    menproducts=menproduct.objects.filter(id=id)
    context={'menproducts':menproducts[0]}
    print(menproducts)
    return render(request,'abc.html',context)

def womenproducts(request,id):
    womproducts=womenproduct.objects.filter(id=id)
    context={'womproducts':womproducts[0]}
    print(womproducts)
    return render(request,'womenproductview.html',context)
    
def kidproducts(request,id):
    kidproducts=kidsproduct.objects.filter(id=id)
    context={'kidproducts':kidproducts[0]}
    print(kidproducts)
    return render(request,'kidsproductview.html',context)
     
    
def women(request):
    womenproducts=womenproduct.objects.all()
    context={'womenproducts': womenproducts}
    print(womenproducts)
    return render(request,'women.html',context)


def kids(request):
    kidsproducts=kidsproduct.objects.all()
    context={'kidsproducts': kidsproducts}
    print(kidsproducts)
    return render(request,'kids.html',context)
    

def home(request):
    return render(request,'home.html')

def electronics(request):

    return render(request,'men.html')

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
        # print("username")
        # print(username)
        # print(password)
        # myshoping=shoping()
        # myshoping.name=username
        # myshoping.password=password
        # myshoping.save()
        

        user=shoping(request, name=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/kids")
        else:
             return redirect("/about")
         
        # user = authenticate(request, name=username, password=password)
        # print(user)

        # if user is not None:
        #     login(request,user)
        #     return redirect("/kids")
        # else:
            
        #     return redirect("/about")
        

def logouthandle(request):
    logout(request)
    messages.success(request,"successfull Logout !!!!")
    return redirect("/home")





