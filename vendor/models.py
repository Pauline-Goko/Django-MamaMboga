from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=64)
    contact = models.CharField(max_length=32)
    store_Name = models.CharField(max_length=32)
    
    # date_created = models.DateTimeField(auto_now_add = True) 
    # date_updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
       
    
