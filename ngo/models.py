from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Ngo(models.Model):
    title = models.CharField(max_length=200)
    Name = models.CharField(max_length=200,default='SOME STRING')
    Phone = models.CharField(max_length=20,default='SOME STRING')
    body = models.TextField()
    Weburl = models.TextField()

    itemImage = models.ImageField(upload_to='images/')
    Id = models.ImageField(upload_to='images/',default='SOME STRING')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)