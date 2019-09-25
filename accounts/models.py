from django.db import models

# Create your models here.

class IUser(models.Model):
    
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    objects = models.Manager()