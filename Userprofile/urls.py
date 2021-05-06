
from django.contrib import admin
from django.urls import path,include
from Userprofile import views

urlpatterns = [
   path('createprofile',views.createprofile,name='createprofile'),
   path('edit1/<int:id>',views.edit,name='edit1'),
   path('<int:request_id>/info',views.info1,name='info1'),
   
  
]