
from django.db import models


# Create your models here.
class Studnet(models.Model):
    firstname=models.CharField(max_length=30,blank=True)
    lastname=models.CharField(max_length=30)
    city=models.CharField(max_length=10)
    per=models.IntegerField()
    
    def __str__(self):
      return self.firstname
