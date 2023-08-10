from django.urls import path
from .views import add_payment, payment_details, edit_payment, payment_list


urlpatterns = [
    path("payment/add", add_payment, name="add_payment_view"),
    path("payment/list", payment_list, name="payment_list_view"),
    path("payment/edit/<int:id>/", edit_payment, name="edit_payment_view"),
    path("payment/<int:id>/", payment_details, name="payment_details_view"),
   
]