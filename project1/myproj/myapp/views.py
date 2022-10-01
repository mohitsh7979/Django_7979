from ast import Delete
from functools import total_ordering
from itertools import product
from json import JSONDecodeError
from sys import stdout
from typing import ValuesView
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.views import View
# from myapp.models import shoping
from myapp.models import *
from math import ceil
from django.db.models import Q
from django.http import JsonResponse
from .forms import CustomUserCreationForm



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
      print(product_id)
      kproduct=kidsproduct.objects.get(id=product_id)
      quantity=kidsproduct.objects.get(id=product_id)
      print(kproduct)
      kcart(user=user,kproduct=kproduct).save()
    #   kcart(user=user,kproduct=kproduct).save()
      
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
    if cart_product or kcart_product or men_cart_product:
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



def logouthandle(request):
    logout(request)
    messages.success(request,"successfull Logout !!!!")
    return redirect("/home")

# def pluscart(request):
#     if request.method=="POST":
#         prod_id=request.POST['prod_id']
    
#         print(prod_id)
#         c=cart.objects.get(Q(wproduct=prod_id) & Q(user=request.user))
#         print(c)
     
#         c.quantity+=1
#         c.save()
#         amount=0.0
#         shipping_amount=70.0
#         cart_product=[p for p in cart.objects.all() if p.user == request.user]
        
#         for p in cart_product:
#             tempamount=(p.wproduct.price)
#             amount+=tempamount
#             total_amount=amount+shipping_amount

#         data = {
#         'quantity':c.quantity,
#         'amount':amount,
#         'totalamount':total_amount
#          }

#         # return JsonResponse(data)
#     return render(request,'men.html')


def checkout(request):
    user=request.user
    add=shoping.objects.filter()
    cart_items=cart.objects.filter()
    kcart_items=kcart.objects.filter()
    mcart_items=mcart.objects.filter()
    amount=0.0
    mamount=0.0
    kamount=0.0
    shipping_amount=70
    total_amount=0.0
    mtotal_amount=0.0
    ktotal_amount=0.0
    whole_amount=0.0
    cart_product=[p for p in cart.objects.all()]
    kcart_product=[p for p in kcart.objects.all()]
    mcart_product=[p for p in mcart.objects.all()]
    if cart_product or kcart_product or mcart_product :
        for p in cart_product:
            tempamount=(p.wproduct.price)
            amount+=tempamount
            total_amount=amount+shipping_amount
            print(total_amount)


        for p in kcart_product:
            print(kcart_product)
            ktempamount=(p.kproduct.price)
            kamount+=ktempamount
            ktotal_amount=kamount+shipping_amount
            print(ktotal_amount)

        for p in mcart_product:
            print(mcart_product)
            mtempamount=(p.mproduct.price)
            mamount+=mtempamount
            mtotal_amount=mamount+shipping_amount
            print(mtotal_amount)


    whole_amount=total_amount+ktotal_amount+mtotal_amount+shipping_amount

    return render(request,'checkout.html',{'add':add,'whole_amount':whole_amount,'cart_items':cart_items,'kcart_items':kcart_items,'mcart_items':mcart_items})



# def payment_done(request):
#     user=request.user
#     custid=request.POST['custid']
#     customer=shoping.objects.get(id=custid)
#     cart_=cart.objects.filter(user=user)
#     for c in cart_:
#         orderplaced(user=user,customer=customer,product=c.wproduct,quantity=c.quantity).save()
#         c.delete()
#     return redirect("orderes")


# def register(request):  
#     if request.POST == 'POST':  
#         form = CustomUserCreationForm()  
#         if form.is_valid():  
#             form.save()  
#             messages.success(request,'Congratualtions!! Registerd Successfull')
#     else:  
#         form = CustomUserCreationForm()  
#     context = {  
#         'form':form  
#     }  
#     return render(request, 'register.html', context)  

class CustomUserCreationView(View):
    def get(self,request):
        form=CustomUserCreationForm()
        messages.success(request,'Congratualtions!! Registerd Successfull')
        return render(request,'register.html',{'form':form})

    def post(self,request):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'register.html',{'form':form})


def profile(request):
    # if request.method=="POST":
    #     name=request.POST['name']
    #     address=request.POST['address'] #+' '+request.POST['address2']
    #     city=request.POST['city']
    #     state=request.POST['state']
    #     zipcode=request.POST['zip']

    #     myuser=shoping(name=name,address=address,city=city,state=state,zipcode=zipcode,address2=address)
    #     myuser.save()

    return render(request,'profile.html')
