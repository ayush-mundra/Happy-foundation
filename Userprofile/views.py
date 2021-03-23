from django.shortcuts import render
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import donator

# name = request.POST['Fname'] and userimage = request.FILES.get('userimg'
# Create your views here.
#@login_required(login_url="/accounts/signup")
def createprofile(request):
    profiles=Profile.objects.all()
    for i in profiles:
        if(i.profile_owner==request.user):
            return render(request, 'donatorpages/home.html',{'error':'your profile already created'})
    
    if request.method == 'POST':
        if request.POST['Fname'] and request.POST['username'] and request.POST['Phone'] and request.POST['state'] and request.POST['city'] :
            profile = Profile()
            profile.Name = request.POST['Fname']
            profile.Username = request.POST['username']
            profile.Phone = request.POST['Phone']
            profile.state = request.POST['state']
            profile.city = request.POST['city']
            profile.owner2 = request.user
            profile.save()
            return redirect('home')

        return render(request, 'Pform.html',{f'error':'All fields are required {}'})        

    return render(request, 'Pform.html')
    
    
def edit(request, id):
    profile= get_object_or_404(Profile,pk=id)
    if request.method=="POST":
        if request.POST['Fname'] and request.POST['Phone'] and request.POST['state'] and request.POST['city'] :
            profile.Name = request.POST['Fname']
            # profile.Username = request.POST['username']
            profile.Phone = request.POST['Phone']
            profile.state = request.POST['state']
            profile.city = request.POST['city']
            profile.profile_owner = request.user
            profile.save()
            return render(request, "index10.html")
            
        return render(request, "index9.html", {"error":"fill all the inputs", "id": id })		
    return render(request, "index9.html",{"id":id})