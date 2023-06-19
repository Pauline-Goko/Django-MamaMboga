from django.contrib import admin
from.models import Shipment

# Register your models here.

class AdminShipment(admin.ModelAdmin):
    list_display = ('location', 'delivery_method', 'shipment_cost', 'status', 'delivery_time', 'delivery_date')

admin.site.register(Shipment, AdminShipment)