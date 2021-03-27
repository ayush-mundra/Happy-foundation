from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Product
import accounts


def allproducts(request):
    products = Product.objects
    return render(request, 'donatorpages/allproduct.html',{'product':products})
def home(request):
    return render(request,'donatorpages/home.html')
def profile(request):
    return render(request,'donatorpages/aboutUser.html',{'User':User})
def Donatorhome(request):
    return render(request,'donatorpages/Donatorhome.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['name'] and request.POST['phone'] and request.POST['address'] and request.FILES['itemimage'] and request.FILES['id']:
            product = Product()
            product.title = request.POST['title']
            product.Name = request.POST['name']
            product.body = request.POST['body']
            product.Phone = request.POST['phone']
            product.address = request.POST['address']
            product.govt_id = request.FILES['id']
            product.itemImage = request.FILES['itemimage']
            product.pub_date = timezone.datetime.now()
            product.product_owner = request.user
            product.save()
            return redirect('/donator/'+ str(product.id))

        return render(request, 'donatorpages/create.html',{'error':'All fields are required'})
    else:
        return render(request, 'donatorpages/create.html')

def details(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'donatorpages/detail.html',{'product':product})
    
def info(request,product_id):
    product = get_object_or_404(Product,pk=product_id)

    return render(request,'donatorpages/info.html',{'product':product})
    
@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.save()
        return redirect('/products/' + str(product.id))
   


@login_required(login_url="/accounts/signup")
def delete(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.pk)
        user.delete()
        #product.save()
        return render(request,'donatorpages/delete.html')

