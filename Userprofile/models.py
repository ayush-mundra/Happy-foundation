
# Create your models here.
# 
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   Name = models.CharField(max_length=200)
   Username = models.CharField(max_length=200)
   Phone = models.CharField(max_length=20)
   state = models.CharField(max_length=200)
   city = models.CharField(max_length=200)
   #owner2 = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
   # country = models.CountryField()

