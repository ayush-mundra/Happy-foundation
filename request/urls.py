from django.urls import path,include
from request import views
urlpatterns = [
    path('needrequest', views.needrequest,name='needrequest'),
    path('delete1', views.delete1, name="delete1"),
    path('edit/<int:id>',views.edit,name='edit'),

    # path('delete1', views.delete1, name="delete1"),
]