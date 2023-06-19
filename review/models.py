from django.db import models

# Create your models here.

class Review(models.Model):
    customer_name = models.CharField(max_length=16)
    message = models.CharField(max_length=300)
    product_name = models.CharField(max_length=120)
    number_of_stars = models.PositiveIntegerField()
    date = models.DateField()
    
    def __str__(self):
        return self.customer_name
