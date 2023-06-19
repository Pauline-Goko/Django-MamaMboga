from django.contrib import admin
from.models import Review

# Register your models here.

class AdminReviews(admin.ModelAdmin):
    list_display = ('customer_name', 'message', 'product_name', 'number_of_stars', 'date')
    
admin.site.register(Review, AdminReviews)
