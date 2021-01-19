from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product
# Create your views here.
def home(request):
    return render(request,'donatorpages/home.html')

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
            product.Id = request.FILES['id']
            product.itemImage = request.FILES['itemimage']
            product.pub_date = timezone.datetime.now()
            product.owner = request.user
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
   