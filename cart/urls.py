from django.urls import path
from .views import view_cart
from .views import cart_list, cart_details, edit_cart




urlpatterns = [
    path("carts/upload", view_cart, name="view_cart_view"),
    path("carts/list", cart_list, name="cart_list_view"),
    path("cart/<int:id>/", cart_details, name="cart_details_view"),
    path("cart/edit/<int:id>/", edit_cart, name="edit_cart_view")

]