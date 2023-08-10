from django.urls import path
from .views import customer_list
from .views import add_customer
from .views import edit_customer
from .views import customer_details


urlpatterns = [
    path("customer/list", customer_list, name="customer_list_view"),
    path("customer/add", add_customer, name="add_customer_view"),
    path("customer/edit/<int:id>/", edit_customer, name="edit_customer_view"),
    path("customer/<int:id>/", customer_details, name="customer_details_view"),
]