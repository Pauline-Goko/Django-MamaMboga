from django.db import models    #module--a file containing methods

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 32)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    stock = models.PositiveIntegerField()
    
    # its important to have the timestamp
    date_created = models.DateTimeField(auto_now_add = True) 
    date_updated = models.DateTimeField(auto_now = True)
     
    # create a string representation of the object
    # inheriting 
    def __str__(self):
        return self.name
    
    
