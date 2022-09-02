from django.contrib import admin


from.models import *

# Register your models here.
# admin.site.site_header="My Login"
# admin.site.register(Studnet)

@admin.register(Studnet)
class StudentAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","city")
    list_filter=("per","city")