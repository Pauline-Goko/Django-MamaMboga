from django.urls import path
from .views import review_details, review_list, edit_reviews, add_review


urlpatterns = [
    path("review/add", add_review, name="add_review_view"),
    path("review/list", review_list, name="review_list_view"),
    path("review/<int:id>/", review_details, name="review_details_view"),
    path("review/edit/<int:id>/", edit_reviews, name="edit_reviews_view")
]