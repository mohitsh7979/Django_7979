from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    course=models.CharField(max_length=50)
    