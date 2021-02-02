from django.urls import path,include
from request import views
urlpatterns = [
    path('needrequest', views.needrequest,name='needrequest'),
]