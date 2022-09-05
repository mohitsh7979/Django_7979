from django.contrib import admin


from .models import *

# Register your models here.
# admin.site.register(student)

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','course']
