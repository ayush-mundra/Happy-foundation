
# Create your models here.
# 
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   Name = models.CharField(max_length=200,default='SOME STRING')
   Username = models.CharField(max_length=200,default='SOME STRING')
   Phone = models.CharField(max_length=20,default='SOME STRING')
   address = models.CharField(max_length=200,default='SOME STRING')
   Userimg = models.ImageField(upload_to='images/')
   owner = models.ForeignKey(User, on_delete=models.CASCADE)
   # country = models.CountryField()

