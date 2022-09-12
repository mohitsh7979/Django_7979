from django.db import models

# Create your models here.
class shoping(models.Model):
    name=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)

