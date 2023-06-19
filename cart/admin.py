from django.contrib import admin
from.models import Cart

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('products_total', 'number_of_products', 'shipping_cost', 'delivery_method', 'payment_method')
    
admin.site.register(Cart, CartAdmin)