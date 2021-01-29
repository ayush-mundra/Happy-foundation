from django.urls import path,include
from request import views
urlpatterns = [
    path('needrequest', views.needrequest,name='needrequest'),
    path('<int:request_id>',views.reqdetails,name='reqdetails'),
]