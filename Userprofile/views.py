from django.shortcuts import render
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# name = request.POST['Fname'] and userimage = request.FILES.get('userimg'
# Create your views here.
#@login_required(login_url="/accounts/signup")
def createprofile(request):
    if request.method == 'POST':
        if request.POST['Fname'] and request.POST['username'] and request.POST['Phone'] and request.POST['state'] and request.POST['city'] :
            profile = Profile()
            profile.Name = request.POST['Fname']
            profile.Username = request.POST['username']
            profile.Phone = request.POST['Phone']
            profile.state = request.POST['state']
            profile.city = request.POST['city']
            profile.save()
            return redirect('edit')

#return redirect('/profile/edit')
        return render(request, 'Pform.html',{f'error':'All fields are required {}'})
    else:
        return render(request, 'Pform.html')
   
    return render(request,'createprofile.html')
def edit(request,user_id):
    user= get_object_or_404(Profile,pk=user_id)
    return render(request,'edit.html',{'Profile':user})

    # def details(request,product_id):
    #     product = get_object_or_404(Product,pk=product_id)

    # return render(request,'donatorpages/detail.html',{'product':product})

#adding comment to check for PR