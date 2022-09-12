from django.db import models

# Create your models here.
class shoping(models.Model):
    user_name=models.CharField(max_length=10)
    password=models.IntegerField()
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)

