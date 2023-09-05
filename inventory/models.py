from django.db import models    #module--a file containing methods
from vendor.models import Vendor
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 32)
    vendor = models.ForeignKey(Vendor, 
                               on_delete=models.CASCADE)
    description = models.TextField()
    product_id = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    stock = models.PositiveIntegerField()
    
    
    # its important to have the timestamp
    date_created = models.DateTimeField(auto_now_add = True) 
    date_updated = models.DateTimeField(auto_now = True)
     

    def __str__(self):
        return self.title
    
    
    
