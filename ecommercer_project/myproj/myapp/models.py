from distutils.command.upload import upload
from random import choices
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.\
CATEGORY_CHOICES=(
    ('m','men'),
    ('w','women'),
    ('k','kids'),
    ('mk','men kit'),
    ('wt','watch'),
)


class product(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.CharField(max_length=10000)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    image=models.ImageField(upload_to='productimage')

    def __str__(self):
        return str(self.id)

class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    product=models.ForeignKey(product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
