from django.contrib import admin
from.models import Notification
# Register your models here.

class AdminNotification(admin.ModelAdmin):
    list_display = ('customer_name', 'time', 'date', 'message', 'order_id')
admin.site.register(Notification, AdminNotification)
