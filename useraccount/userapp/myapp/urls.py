from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from myapp import views
from .views import *

urlpatterns = [
    path('',views.index,name="home"),
    path('login/',views.login,name="login"),
    path('logout/',views.logoutuser,name="logout"),
]
