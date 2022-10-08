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
from django import views
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.getproduct.as_view()),
    path('home/',views.getproduct.as_view()),
    path('men/',views.menproduct.as_view()),
    path('women/',views.womenmenproduct.as_view()),
    path('kids/',views.kidproduct.as_view()),
    path('abc/<int:id>',views.productview.as_view()),
    path('addtocart/',views.addtocart),
    path('showcart/',views.showcart),
    path('order/',views.order)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
