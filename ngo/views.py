
from django.contrib import  admin
from django.urls import path, include
from ngo import views
from django.conf import settings
from django.conf.urls.static import static
from ngo.models import Products
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from Userprofile.models import Profile


def homes(request):
    products = Products.objects
    #curr_user= request.user
    #obj = get_object_or_404(Profile, pk=curr_user.id
    return render(request,'ngopages/home.html',{'products':products})


def help(request):
    if request.method == 'POST':
        if request.POST['Fname'] and request.POST['username'] and request.POST['Phone'] and request.POST['state'] and request.POST['city'] :
            product = Products()
            product.Name = request.POST['Fname']
            product.Username = request.POST['username']
            product.Phone = request.POST['Phone']
            product.state = request.POST['state']
            product.city = request.POST['city']
            #product.owner1=request.user
            product.save()
            return redirect("home")
   
        return render(request, 'ngopages/help.html',{f'error':'All fields are required {}'})
    else:
        return render(request, 'ngopages/help.html')
   
