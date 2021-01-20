
from django.contrib import  admin
from django.urls import path, include
from ngo import views
from django.conf import settings
from django.conf.urls.static import static
from donator.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone


def homes(request):
    products = Product.objects
    return render(request,'ngopages/home.html',{'products':products})

def help(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['name'] and request.POST['phone'] and request.POST['address'] and request.FILES['insideImage'] and request.FILES['Id']:
            product = Product()
            product.title = request.POST['title']
            product.Name = request.POST['name']
            product.body = request.POST['body']
            product.Phone = request.POST['phone']
            product.address = request.POST['address']
            product.Id = request.FILES['id']
            product.itemImage = request.FILES['insideImage']
            product.pub_date = timezone.datetime.now()
            product.owner = request.user
            product.save()
            return redirect('/donator/'+ str(product.id))
