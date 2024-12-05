#Importing all the dependencies
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Needrequest
from Userprofile.models import Profile
import donator;
import Userprofile;

# Need request function helps in posting request for any object which a user needs
@login_required
def needrequest(request):
    #If request method is post
    if request.method == 'POST':
        # checking whether no field is empty in the form
        if  request.POST.get("title",False) and request.POST.get("body", False) and request.POST.get('name', False) and  request.POST.get('phone', False):
            _request =  Needrequest()
            #getting all attributes of the request object which are in form data
            _request.title = request.POST.get('title',False)
            _request.body = request.POST.get('body', False)
            _request.name = request.POST.get('name', False)
            _request.phone = request.POST.get('phone', False)
            _request.pub_date = timezone.datetime.now()
            _request.needy = request.user
            # a loop to check whether the user who is requesting for the objects has created  a profile or not for security/privacy purpose
            #if he is registered then we will allow him to post a request
            for i in Profile.objects.all():
                if(i.profile_owner==_request.needy):
                    _request.save()
                    return render(request, 'req_details.html',{"request": _request})
                
            #if the user has not created the profile then we will give him a message to create profile
            return render(request, 'Pform.html',{'error':'create your profile first'}) 
        
        #if all fields are not filled then we will display fill all fields
        return render(request, 'need_request.html',{'error':'All fields are required'})
    
    return render(request, 'need_request.html')

#this method will delete the request
def delete1(request):
        if request.method=="POST":
            #we will iterate over all the request and will delete that request which is created by user
            for req in Needrequest.objects.all():
                #here user is current user and needy is an attribute associated with every request which stores the id/name of user who has create it
                if(request.user== req.needy):
                    #deleting the request object
                    req.delete() 
                    #after that rendering the user to the new html file
                    return render(request, 'delete1.html')
                
                
#if we want to see our reqest through url then we will have to pass the request id  
def info1(request, request_id):
    request1 = get_object_or_404(Needrequest,pk= request_id)
    return render(request,'info1.html',{'request':request1})

#deleting the request with url by passing id
def delete(request, request_id):
        request1 = get_object_or_404(Needrequest,pk= request_id)
        request1.delete()
        return redirect('displayrequest')


#This method is to edit a particular request through url by passing id
def edit(request, id):
    #this will fetch the object form the collection Needrequest
    _request = get_object_or_404(Needrequest, pk=id)
    
    #the user will fill the form and we will recieve his data
    if request.method=="POST":
        if request.POST.get("title",False) and request.POST.get("body", False) and request.POST.get('name', False) and request.POST.get('phone', False):
            #updating all the attributes
            _request.title = request.POST.get('title',False)
            _request.body = request.POST.get('body', False)
            _request.phone = request.POST.get('phone', False)
            _request.name = request.POST.get('name', False)
            _request.pub_date = timezone.datetime.now()
            _request.needy = request.user
            #finally saving the request
            _request.save()
            return redirect('displayrequest')
            
        return render(request, "index7.html", {"error":"fill all the inputs", "id": id })	
    
    #before post request this page will be rendered and it contains form
    return render(request, "index7.html",{"id":id})

#this method displays all the requests which are there in the collection Needrequest.
def displayrequest(request):
    request1 = Needrequest.objects.all()
    return render(request,'displayrequest.html',{'requests':request1})
