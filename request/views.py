from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Needrequest
from Userprofile.models import Profile


@login_required
def needrequest(request):
    if request.method == 'POST':
        if request.POST.get("title",False) and request.POST.get("body", False):
            request1 = Needrequest()
            request1.title =  request.POST.get("title", "Guest (or whatever)")
            request1.body = request.POST.get('body', False)
            request1.pub_date = timezone.datetime.now()
            request1.needy = request.user
            request1.save()
            for i in Profile.objects.all():
                if(i.owner2==request1.needy):
                    return render(request,"req_details.html",{"request": request1,"user":i})
        
        return redirect("home")
        #return render(request, 'need_request.html',{'error':'All fields are required'})
        
    return render(request, 'need_request.html')
    
def delete1(request):
    if request.method=="POST":
        for profile in Profile.objects.all():
            if(request.user==profile.owner2):
                profile.delete()
                # bhia user create he nahi hoga tho delete ka buttin 
                #BAAD ME YAHA CHANGES KARENGE
                return render('delete1.html')



            

    
