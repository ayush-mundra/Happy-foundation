
# Create your models here.
# 
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   # Profile_id = models.AutoField(primary_key=True, default=None)
   Name = models.CharField(max_length=200)
   Phone = models.CharField(max_length=20)
   state = models.CharField(max_length=200)
   city = models.CharField(max_length=200)
   profile_owner = models.ForeignKey(User, on_delete=models.CASCADE,default=0)


