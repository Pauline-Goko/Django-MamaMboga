from django.db import models

# Create your models here.

class Notifications(models.Model):
    customer_name = models.CharField(max_length=40)
    message = models.CharField(max_length=120)
    time = models.TimeField()
    date = models.DateField()
    order_id = models.PositiveIntegerField()
    
    def __str__(self):
        return self.customer_name
 
    
