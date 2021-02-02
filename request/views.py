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
        if  request.POST.get('body', False):
            _request =  Needrequest()
            _request.title = request.POST['title']
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


# def reqdetails(request,):
#       _request = get_object_or_404(Needrequest,pk=request_id)
#       profile = get_object_or_404(Profile,pk=user_id)
#       return render(request,'req_details.html',{'request':_request,'user':profile})
#     #   what?