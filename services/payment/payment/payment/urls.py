from django.urls import path

from payment.payment.v1.views import PaymentView, PaymentOrderView

urlpatterns = [
    path('v1/create/', view=PaymentView.as_view(), name='payment_create'),
    path('v1/update/<int:id>/', view=PaymentView.as_view(), name='payment_update'),
    path('v1/order/<int:order>/update/', view=PaymentOrderView.as_view(), name='order_payment_update'),
    path('v1/<int:id>/', view=PaymentView.as_view(), name='payment_detail'),
    path('v1/order/<int:order>/', view=PaymentOrderView.as_view(), name='order_payment_detail'),
]
