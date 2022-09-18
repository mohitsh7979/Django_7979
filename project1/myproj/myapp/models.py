from distutils.command.upload import upload
from email.policy import default
from turtle import title
from django.db import models

# Create your models here.
class shoping(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
   

    def __str__(self):
        return self.name

class product(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=50)
    image=models.ImageField(upload_to="menimg/images")

    def __str__(self):
        return self.title

class womenproduct(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=50)
    image=models.ImageField(upload_to="womenimg/images")

    def __str__(self):
        return self.title
    
class kidsproduct(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=50)
    image=models.ImageField(upload_to="kidsimg/images")

    def __str__(self):
        return self.title

    
    


    



