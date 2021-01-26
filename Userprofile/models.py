
# Create your models here.
# name = request.POST.get('Fname'),userimage = request.FILES.get('userimg')
from django.db import models
from django.contrib.auth.models import User
# from django_countries.fields import CountryField




# Create your models here.
class Profile(models.Model):
   Name = models.CharField(max_length=200,default='SOME STRING')
   Phone = models.CharField(max_length=20,default='SOME STRING')
   address = models.CharField(max_length=200,default='SOME STRING')
   Userimg = models.ImageField(upload_to='User/')
   # country = models.CountryField()

