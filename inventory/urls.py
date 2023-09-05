from django.urls import path
from .views import upload_product
from .views import products_list
from .views import product_details
# from .views import edit_product

urlpatterns = [
    path("products/upload", upload_product, name="product_upload_view"),
    path("products/list", products_list, name="products_list_view"),
    path("products/<int:id>/", product_details, name = "product_details_view"),
    # path("products/edit/<int:id>/", edit_product, name = "edit_product_view")
]







# path for the request