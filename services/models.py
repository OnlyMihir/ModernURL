from django.db import models

# Create your models here.

class shortenedurl(models.Model):
    
    user_id = models.IntegerField()
    sh_url = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    org_url = models.CharField(max_length=50)
    is_ent_user = models.BooleanField(default=False)
    objects = models.Manager()