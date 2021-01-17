from django.contrib import admin
from django.urls import path, include
from .views import pay, success

urlpatterns = [
   path('pay',pay,name='pay'),
    path('success' , success , name='success')
  
]