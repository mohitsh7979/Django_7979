from sre_constants import CATEGORY
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from math import ceil



# Create your views here.
class getproduct(View):
    
  def get(self,request):
    menkit=product.objects.filter(category='mk')
    men=product.objects.filter(category="m")
    n= len(menkit)
    nSlides= n//4 + ceil((n/4) + (n//4))
    context={'no_of_slides':nSlides, 'range':range(1,nSlides), 'menkit': menkit,'men':men}
    print(menkit)
    print(men)
    
    print(context)
    return render(request,'content.html',context)

class menproduct(View):
    def get(self,request):
        men=product.objects.filter(category="m")
        context={'men':men}
        return render(request,'men.html',context)

class womenmenproduct(View):
    def get(self,request):
        women=product.objects.filter(category="w")
        print(women)
        context={'women':women}
        return render(request,'women.html',context)

class kidproduct(View):
    def get(self,request):
        kid=product.objects.filter(category="k")
        context={'kid':kid}
        return render(request,'kids.html',context)

class productview(View): 
        
 def get(self,request,id):
    prod=product.objects.get(id=id)
    print(prod)
    context={   
        'prod':prod
        
    }
    print(prod)
    return render(request,'productview.html',context)

def addtocart(request):
    if request.method=="POST":
      user=request.user
      product_id=request.POST['prod_id']
      products=product.objects.get(id=product_id)
      cart(user=user,product=products).save()



    return redirect("/showcart")

def showcart(request):
      user=request.user
      Cart=cart.objects.filter(user=user)
      context={'Cart':Cart}
      amaount=0.0
      total_amount=0.0
      shipping_amount=70.0
      cart_product=[p for p in cart.objects.all() if p.user==user]
    
      if cart_product:
        for p in cart_product:
            tempamount=(p.product.price)
            amaount+=tempamount
            total_amount=amaount+shipping_amount
            context={
                'amount':amaount,
                'total_amount':total_amount,
                'Cart':Cart
            }


      return render(request,'addtocart.html',context)

def order(request):
    # user=request.user
    products=product.objects.filter()
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product=[p for p in product.objects.all() ]
    if cart_product:
        for p in cart_product:
            teampamount=(p.product.price)
            amount+=teampamount
            total_amount=amount+shipping_amount
            context={
                'total_amount':total_amount,
                'products':products

            }
    return render(request,'order.html',context)




    

    




   