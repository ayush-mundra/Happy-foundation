
# Create your models here.
# 
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   Name = models.CharField(max_length=200,default='SOME STRING')
   Username = models.CharField(max_length=200,default='SOME STRING')
   Phone = models.CharField(max_length=20,default='SOME STRING')
   state = models.CharField(max_length=200,default='SOME STRING')
   city = models.CharField(max_length=200,default='SOME STRING')
   # country = models.CountryField()

