from django.urls import path

from cart.cart.v1.views import CartView

urlpatterns = [
    path('v1/create/<int:customer>/', view=CartView.as_view(), name='cart_create'),
    path('v1/<int:customer>/', view=CartView.as_view(), name='cart_detail'),
    path('v1/update/<int:customer>/', view=CartView.as_view(), name='cart_update'),
    path('v1/clear/<int:customer>/', view=CartView.as_view(), name='cart_clear'),
]
