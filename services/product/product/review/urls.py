from django.urls import path

from product.review.v1.views import ReviewCreateView, ReviewListView

urlpatterns = [
    path('v1/create/', view=ReviewCreateView.as_view(), name='review_create'),
    path('v1/list/', view=ReviewListView.as_view(), name='review_list'),
]
