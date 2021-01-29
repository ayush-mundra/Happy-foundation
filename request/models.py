from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Needrequest(models.Model):
   title = models.CharField(max_length=200,default='SOME STRING')
   pub_date = models.DateTimeField() 
   body = models.CharField(max_length=200,default='SOME STRING')
   needy = models.ForeignKey(User, on_delete=models.CASCADE)

