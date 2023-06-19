from django.contrib import admin
from.models import Notifications

# Register your models here.

class AdminNotifications(admin.ModelAdmin):
    list_display = ('customer_name', 'time', 'date', 'message', 'order_id')
    
    
admin.site.register(Notifications, AdminNotifications )
