from django.urls import path

from .views import *

urlpatterns = [
    path('',profile_create,name='profile'),
    path('saved/',SaveProfile,name='saved'),
]
