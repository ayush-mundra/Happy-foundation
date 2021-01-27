from django.shortcuts import render
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# name = request.POST['Fname'] and userimage = request.FILES.get('userimg'
# Create your views here.
def createprofile(request):
    if request.method == 'POST':
        if request.POST['Fname'] and request.POST['username'] and request.POST['Phone'] and request.POST['stt'] :
            profile = Profile()
            profile.Name = request.POST['Fname']
            profile.Username = request.POST['username']
            profile.Phone = request.POST['Phone']
            profile.address = request.POST['stt']
            product.Userimg = request.FILES['userimg']
            # profile.Userimg = request.FILES.get('userimg',False)  and request.FILES.get('userimg',False)
            profile.save()
            return redirect('/profile/edit')


        return render(request, 'Pform.html',{f'error':'All fields are required {}'})
    else:
        return render(request, 'Pform.html')
   
    return render(request,'createprofile.html')
def edit(request):
    return render(request,'edit.html',{'Profile':Profile})
