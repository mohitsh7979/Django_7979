"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from httplib2 import Authentication
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from myapp.forms import LoginForm



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home/',views.home),
    path('men/',views.men),
    path('women/',views.women),
    path('kids/',views.kids),
    path('new/',views.new),
    path('add/',views.add),
    path('cart/',views.showcart),
    path('profile/',views.profile,name="profile"),
    # path('abc/',views.abc,name="abc"),
   
    # path('login',views.loginhandle,name="loginhandle"),
    path('logout/',views.logouthandle,name="logouthandle"),
    path('abc/<int:id>',views.abc,name="abc"),
    path('womenproduct/<int:id>',views.womenproducts,name="womenproducts"),
    path('kidproduct/<int:id>',views.kidproducts,name="kidproducts"),
    path('buy/',views.buynow,name="bynow"),
    path('add-to-cart/',views.addtocart,name="addtocart"),
    path('add-to-cart-k/',views.addtokcart,name="addtokcart"),
    path('add-to-cart-m/',views.addtomcart,name="addtomcart"),
    path('checkout/',views.checkout,name="checkout"),
    # path('pluscart',views.pluscart,name="pluscart"),
    # path('register/',views.register,name="register"),
    path('register/',views.CustomUserCreationView.as_view(),name="customercreationform"),
    path('account/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name="loginform")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
