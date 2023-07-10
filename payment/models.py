from django.db import models


# Create your models here.

class Payment(models.Model):
    payment_choices = (
        ('M-pesa', 'M-Pesa'),
        ('Pay on Delivery', 'Pay on Delivery'),
    )
    payment_method = models.CharField(max_length=64, choices=payment_choices)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_time = models.TimeField()
    payment_date = models.DateField()
    receipt_number = models.CharField(max_length=32)
    status = models.CharField(max_length=15)
    reference_number = models.CharField(max_length=32)
    products= models.CharField(max_length=64)
    refunds = models.CharField(max_length=500)
    
    def __str__(self):
        return self.payment_method
    
