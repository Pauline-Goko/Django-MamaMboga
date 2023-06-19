from django.db import models

# Create your models here.

class Shipment(models.Model):
    location = models.CharField(max_length=120)
    delivery_choices = (
        ('Pick-up Point', 'Pick-up Point'),
        ('Home Delivery', 'Home Delivery'),
    )
    delivery_method = models.CharField(max_length=64, choices=delivery_choices)
    shipment_cost = models.PositiveIntegerField()
    status = models.CharField(max_length=12)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    
    def _str__(self):
        return self.location

