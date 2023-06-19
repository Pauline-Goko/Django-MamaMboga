from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length = 16)
    order_number = models.PositiveIntegerField()
    order_total = models.DecimalField(max_digits = 6, decimal_places = 2)
    order_date = models.DateField()
    location = models.CharField(max_length = 64)
    delivery_choices = (
        ('Pick-Up Point', 'Pick-Up Point'),
        ('Home Delivery', 'Home Delivery'),
    )
    delivery_method = models.CharField(max_length=15, choices=delivery_choices)
    
    delivery_date = models.DateField()
    
    # date_created = models.DateTimeField(auto_now_add = True) 
    # date_updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
    
    
