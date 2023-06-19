from django.contrib import admin
from.models import Payment

# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'payment_method', 'payment_date','receipt_number', 'status', 'products', 'reference_number')
    
    
admin.site.register(Payment, PaymentAdmin)
