from django.contrib import admin
from.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_number', 'order_total', 'order_date', 'delivery_method', 'delivery_date')
      
      
    #   register
admin.site.register(Order, OrderAdmin)
