from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import need_request

@login_required
# products hata  line 14
def need_request(request):

    if request.method == 'POST':
        if request.POST['title'] and request.POST['name'] and request.POST['phone'] and request.POST['address'] and request.FILES['id']:
            product = Product() 
            product.title = request.POST['title']
            product.Name = request.POST['name']
            product.body = request.POST['body']
            product.Phone = request.POST['phone']
            product.address = request.POST['address']
            product.Id = request.FILES['id']
            product.itemImage = request.FILES['itemimage']
            product.pub_date = timezone.datetime.now()
            product.owner = request.user
            product.save()
            return redirect('/donator/'+ str(product.id))


        return render(request, 'donatorpages/need_request.html',{'error':'All fields are required'})
    else:
        return render(request, 'donatorpages/need_request.html')