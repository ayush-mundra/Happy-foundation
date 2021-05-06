
from django.contrib import admin
from django.urls import path,include
from donator import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include("Home.urls")),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/', include('accounts.urls')),
    path('donator/', include('donator.urls')),
    path('razor/', include('razorpay.urls')),
    path('ngo/', include('ngo.urls')),
    path('profile/', include('Userprofile.urls')),
    path('request/', include('request.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)