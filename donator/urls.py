
from django.contrib import admin
from django.urls import path, include
from donator import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('create',views.create,name='create'),
   path('home',views.home, name='home'),
   path('Donatorhome',views.Donatorhome, name='Donatorhome'),
   path('<int:product_id>',views.details,name='details'),
   path('<int:product_id>/info',views.info,name='info'),
   path('delete',views.delete,name='delete'),
      #path('allproducts',views.allproducts, name='allproducts'),
   #path('profile',views.profile, name='profile'),

 
]
