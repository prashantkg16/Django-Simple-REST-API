from django.db import models

# Create your models here.
class router(models.Model):
    class Meta:
        verbose_name = "Manage Router"
    sapid =  models.CharField(max_length=20, unique=True)    
    hostname =  models.CharField(max_length=16, unique=True)
    loopback =  models.CharField(max_length=16)
    macaddress = models.CharField(max_length=24)