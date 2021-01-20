from django.contrib import admin
from django.urls import path,include
from ngo import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('homes',views.homes, name='homes'),
  path('help',views.help, name='help'),
    ]