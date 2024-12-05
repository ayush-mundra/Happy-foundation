from django.contrib import admin
from django.urls import path,include
from ngo import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  #ye maine kiya dekh vo file 
  path('homes',views.homes, name='homes'),
  path('displayItem',views.displayItem, name='displayItem'),
  path('help',views.help, name='help'),
  path('<int:ngo_id>/info2',views.info2,name='info2'),
  path('<int:ngo_id>',views.details1,name='details1'),
 
    ]



#adding comment 