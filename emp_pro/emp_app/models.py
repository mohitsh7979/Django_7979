from django.db import models

class Contact(models.Model):
    Email=models.CharField(max_length=122)
    textarea=models.CharField(max_length=122)


# Create your models here.
