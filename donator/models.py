from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
   title = models.CharField(max_length=200)
   Name = models.CharField(max_length=200)
   Phone = models.CharField(max_length=20)
   address = models.CharField(max_length=200)
   pub_date = models.DateTimeField()         
   body = models.TextField()
   itemImage = models.ImageField(upload_to='images/')
   Id = models.ImageField(upload_to='images/')
   owner = models.ForeignKey(User, on_delete=models.CASCADE, default=0)



def  __str__(self):
    return self.title 
def summary(self):
    return self.body[:100]
def pub_date_pretty(self):
    return self.pub_date.strftime("%b %e %Y") 