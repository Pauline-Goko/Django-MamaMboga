from django.urls import path
from .views import add_shipment, shipment_details, edit_shipment, shipment_list


urlpatterns = [
    path("shipment/add", add_shipment, name="add_shipment_view"),
    path("shipment/list", shipment_list, name="shipment_list_view"),
    path("shipment/<int:id>/", shipment_details, name="shipment_details_view"),
    path("shipment/edit/<int:id>/", edit_shipment, name="edit_shipment_view"),
]