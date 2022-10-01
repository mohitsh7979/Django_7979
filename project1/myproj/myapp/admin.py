from django.contrib import admin
from .models import *
 
admin.site.site_header  =  "Regex Shopping" 

# Register your models here.
admin.site.register(shoping)
# admin.site.register(product)
# admin.site.register(womenproduct)
# admin.site.register(kidsproduct)
admin.site.register(order)
admin.site.register(cart)
admin.site.register(kcart)
admin.site.register(mcart)


@admin.register(menproduct)
class productAdmin(admin.ModelAdmin):
    list_display=['id','title']


@admin.register(womenproduct)
class productAdmin(admin.ModelAdmin):
    list_display=['id','title']

@admin.register(kidsproduct)
class productAdmin(admin.ModelAdmin):
    list_display=['id','title']
