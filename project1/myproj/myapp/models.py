from distutils.command.upload import upload

from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User



# # Create your models here.
class shoping(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    # id=models.AutoField(primary_key=True,default=1)
    name=models.CharField(max_length=10,default=0)
    address=models.CharField(max_length=100,default=0)
    # address2=models.CharField(max_length=30)
    city=models.CharField(max_length=30,default=0)
    state=models.CharField(max_length=30,default=0)
    zipcode=models.CharField(max_length=30,default=0)
   

    def __str__(self):
        return self.name

class menproduct(models.Model):
    id=models.AutoField
    title=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=50)
    image=models.ImageField(upload_to="menimg/images")

    def __str__(self):
        return self.title

class womenproduct(models.Model):
    id=models.AutoField
    title=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=50)
    image=models.ImageField(upload_to="womenimg/images")

    def __str__(self):
        return self.title
    
class kidsproduct(models.Model):
    id=models.AutoField
    title=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=50)
    image=models.ImageField(upload_to="kidsimg/images")

    def __str__(self):
        return self.title

class order(models.Model):
    order_id= models.AutoField
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

def __str__(self):
      return self.name

class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    wproduct=models.ForeignKey(womenproduct, on_delete=models.CASCADE)
    # mproduct=models.ForeignKey(menproduct,on_delete=models.CASCADE)
    # kproduct=models.ForeignKey(kidsproduct, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
@property
def total_cost(self):
    return self.wproduct.price

    # def __str__(self):
    #     return self.wproduct

class kcart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    kproduct=models.ForeignKey(kidsproduct, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

# @property
def total_cost_k(self):
    return self.kproduct.price
    def __str__(self):
        return self.kproduct

class mcart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    mproduct=models.ForeignKey(menproduct, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

# # @property
# def total_cost_m(self):
#     return self.mproduct.price
    # def __str__(self):
    #     return self.mproduct


    # def __str__(self):
    #     return self.user

# class orderplaced(models.Model):
#     customer=models.CharField(max_lenght=100)








    
    


    



