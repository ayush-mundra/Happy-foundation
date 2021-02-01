from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Ngoprofile(models.Model):
    Name = models.CharField(max_length=200)
    Username = models.CharField(max_length=200)
    Phone = models.CharField(max_length=20)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    owner1 = models.ForeignKey(User, on_delete=models.CASCADE,default=1)