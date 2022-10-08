from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=['id','title','price','category','image']

@admin.register(cart)
class cartAdmin(admin.ModelAdmin):
    list_display=['id','quantity','product']