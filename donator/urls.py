
from django.contrib import admin
from django.urls import path, include
from donator import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('create',views.create,name='create'),
#    path('',views.create,name='home'),
    path('home',views.home, name='home'),
   path('<int:product_id>',views.details,name='details'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
 
]