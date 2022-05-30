from django.urls import path

from ordering.ordering.v1.views import OrderPlaceView, OrderCancelView

urlpatterns = [
    path('v1/place/', view=OrderPlaceView.as_view(), name='create_order'),
    path('v1/cancel/', view=OrderCancelView.as_view(), name='cancel_order'),
]