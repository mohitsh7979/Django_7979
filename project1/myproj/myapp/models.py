from distutils.command.upload import upload
import email
from email.policy import default
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.
class shoping(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
   

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
    order_id= models.AutoField(primary_key=True)
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

    def __str__(self):
        return self.wproduct

class kcart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    kproduct=models.ForeignKey(kidsproduct, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.kproduct

class mcart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    mproduct=models.ForeignKey(menproduct, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.mproduct


    # def __str__(self):
    #     return self.user







    
    


    



