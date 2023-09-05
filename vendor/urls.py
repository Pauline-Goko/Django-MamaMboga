from django.urls import path
from .views import add_vendor,  vendor_list, vendor_details


urlpatterns = [
    path("vendor/add", add_vendor, name="add_vendor_view"),
    path("vendor/list", vendor_list, name="vendor_list_view"),
    path("vendor/<int:id>/", vendor_details, name="vendor_details_view"),
   
]