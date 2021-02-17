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
        if  i request.POST.get('body', False)::
            _request =  Needrequest()
            _request.title = request.POST.get('title',False)
            _request.body = request.POST.get('body', False)
            _request.pub_date = timezone.datetime.now()
            _request.needy = request.user
            _request.save()
            for i in Profile.objects.all():
                if(i.owner2==request.user):
                    return render(request, 'req_details.html',{"request": _request,"user":i})
        return render(request, 'need_request.html',{'error':'All fields are required'})
    else:
        return render(request, 'need_request.html')


def delete1(request):
    if request.method=="POST":
        for profile in Profile.objects.all():
            if(request.user==profile.owner2):
                profile.delete()
                # bhia user create he nahi hoga tho delete ka buttin 
                #BAAD ME YAHA CHANGES KARENGE
                return render('delete1.html')



            

    
