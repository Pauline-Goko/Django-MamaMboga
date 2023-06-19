from django.db import models

# Create your models here.

class Cart(models.Model):
    delivery_choices = (
        ('Pick-Up Point', 'Pick-Up Point'),
        ('Home Delivery', 'Home Delivery'),
    )
    delivery_method = models.CharField(max_length=15, choices=delivery_choices)
    number_of_products = models.IntegerField()
    products_total = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    
    payment_choice = (
        ('M-Pesa', 'M-Pesa'),
        ('Pay on Delivery', 'Pay on Delivery'),
    )
    payment_method = models.CharField(max_length = 15, choices = payment_choice)
    
    def __str__(self):
        return self.delivery_options
