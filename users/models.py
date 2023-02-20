from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser (AbstractUser) :
    age = models.PositiveIntegerField(null=True,blank=True)
    number = models.CharField(null =False,blank=False,max_length=50,default='01127210144')