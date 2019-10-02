from django.db import models
from datetime import datetime

# Create your models here.

class shortenedurl(models.Model):
    
    user_id = models.IntegerField()
    sh_url = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    org_url = models.CharField(max_length=50)
    is_ent_user = models.BooleanField(default=False)
    objects = models.Manager()

class ent_url_data(models.Model):
    sh_url = models.CharField(max_length=50)
    continent = models.CharField(max_length=100,blank=True,null=True)
    state_region = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    postal_code = models.CharField(max_length=100,blank=True,null=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    objects = models.Manager()