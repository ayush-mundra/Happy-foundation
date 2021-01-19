
from django.contrib import  admin
from django.urls import path, include
from donator import views
from django.conf import settings
from django.conf.urls.static import static
from donator.models import Product
from django.shortcuts import render


def homes(request):
    products = Product.objects
    return render(request,'ngopages/home.html',{'products':products})