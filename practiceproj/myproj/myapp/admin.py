from django.contrib import admin
from.models import *



# Register your models here.
# admin.site.register(students)

@admin.register(students)
class studentadmin(admin.ModelAdmin):
    list_display=("name","age")