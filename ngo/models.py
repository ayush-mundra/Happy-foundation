from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Ngoprofile(models.Model):
    Name = models.CharField(max_length=200)
    certificates = models.ImageField(upload_to='images/', default=None)
    Phone = models.CharField(max_length=20)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    ngo_creator = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
