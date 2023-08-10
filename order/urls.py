from django.urls import path
from .views import order_details, order_list, add_order,edit_order


urlpatterns = [
    path("order/list", order_list, name="order_list_view"),
    path("order/add", add_order, name="add_order_view"),
    path("order/edit/<int:id>/", edit_order, name="edit_order_view"),
    path("order/<int:id>/", order_details, name="order_details_view"),
]

