
from django.urls import path,include

from . import views

urlpatterns = [
   path('create',views.create,name='create'),
#    path('',views.create,name='home'),
    path('home',views.home, name='home'),
   path('<int:product_id>',views.details,name='details'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
 
]
