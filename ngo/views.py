from django.contrib import  admin
from django.urls import path, include
from ngo import views
from django.conf import settings
from django.conf.urls.static import static
from donator.models import Product
from ngo.models import Ngoprofile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from Userprofile.models import Profile
# Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
# https://docs.djangoproject.com/en/3.1/topics/db/queries/
def homes(request):
    ngopro = Ngoprofile.objects.all()
    profile_set= Profile.objects.filter(profile_owner=request.user)
    return render(request,'ngopages/homes.html',{'ngos':ngopro,"profile_set":profile_set  })
    # curr_user= request.user
    # profiles = Profile.objects.all()
    # res=[]
    # if( len(ngopro.filter(owner1=curr_user)) != 0):
    #     curr_user = ngopro.filter(owner1=curr_user)[0]
    #     print(curr_user)
    #     for i in profiles:     
    #         if curr_user.city == i.city:
    #             res.append(i)   
    # return render(request,'ngopages/home.html',{'products':ngopro,"res": res })
    # ngopro = Ngoprofile.objects.all()
    # curr_user= request.user
    # profiles = Profile.objects.all()
    # res=[]
    # if( len(ngopro.filter(owner1=curr_user)) != 0):
    #     curr_user = ngopro.filter(owner1=curr_user)[0]
    #     print(curr_user)
    #     for i in profiles:     
    #         if curr_user.city == i.city:
    #             res.append(i)   
    # return render(request,'ngopages/home.html',{'products':ngopro,"res": res })
# entry_list = list(Entry.objects.all())
# for e in Entry.objects.all():
#    print(e.headline)
# 
#        print("There is at least one Entry with the headline Test")


    # q1 = profiles.filter()
   
    # for i in profiles:
    #     if(i.owner2==curr_user):
    #         CITY=i.city   
    # x         
def displayItem(request):
    products = Product.objects
    return render(request,'ngopages/displayitem.html',{'products':products})

# def donateto(request):

def help(request):
    if request.method == 'POST':
        if request.POST['Fname'] and request.FILES['certificates'] and request.POST['Phone'] and request.POST['state'] and request.POST['city'] :
            product = Ngoprofile()
            product.Name = request.POST['Fname']
            product.certificates = request.FILES['certificates']
            product.Phone = request.POST['Phone']
            product.state = request.POST['state']
            product.city = request.POST['city']
            product.ngo_creator=request.user
            product.save()
            return redirect('/ngo/'+ str(product.id)+'/info2')
   
        return render(request, 'ngopages/help.html',{f'error':'All fields are required {}'})
    else:
        return render(request, 'ngopages/help.html')

def info2(request, ngo_id):
    ngo = get_object_or_404( Ngoprofile, pk=ngo_id)
    return render(request,'ngopages/info2.html',{'ngo':ngo})
    
    
def details1(request, ngo_id):
    ngo = get_object_or_404( Ngoprofile, pk=ngo_id)
    return render(request,'ngopages/aboutngo.html',{'ngo':ngo})
   
# 2405:201:4:90c2:8ca5:e316:c8c1:c901
# http://127.0.0.1:8000/