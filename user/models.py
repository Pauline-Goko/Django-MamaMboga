from django.db import models

# Create your models here.


class User (models.Model):
    name = models.CharField(max_length=32)
    phone_Number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=32)
    
    
    def __str__(self):
        return self.name
    
