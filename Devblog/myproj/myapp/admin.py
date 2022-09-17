from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(signup)
admin.site.register(Post ,PostAdmin)
