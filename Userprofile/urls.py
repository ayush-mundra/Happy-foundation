
from django.contrib import admin
from django.urls import path,include
from Userprofile import views

urlpatterns = [
   path('createprofile',views.createprofile,name='createprofile'),
   path('<int:user_id>/edit',views.edit,name='edit'),
   # <int:product_id>
   
  
]