from django.db import models
from payment.models import Payment
from inventory.models import Product
from customer.models import Customer
from shipment.models import Shipment
from cart.models import Cart



# Create your models here.

class Order(models.Model):
    # name = models.CharField(max_length = 16)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart,
                             on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product,
                                 on_delete=models.CASCADE, null=True )
    order_number = models.PositiveIntegerField()
    order_total = models.DecimalField(max_digits = 6, decimal_places = 2)
    order_date = models.DateField()
    # location = models.CharField(max_length = 64)
    delivery_choices = (
        ('Pick-Up Point', 'Pick-Up Point'),
        ('Home Delivery', 'Home Delivery'),
    )
    delivery_method = models.CharField(max_length=15, choices=delivery_choices)
    shipment = models.ForeignKey(Shipment,
                                 on_delete=models.CASCADE, null=True)
    
    delivery_date = models.DateField()
    payment = models.ForeignKey(Payment,
                                   on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        # return self.customer
         return f"Order #{self.pk}"
    
    
