from django.contrib import admin
from.models import Vendor

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact', 'store_Name')
    
    
admin.site.register(Vendor, VendorAdmin)
