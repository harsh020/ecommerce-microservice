from django.urls import path

from order.order.v1.views import OrderCreateView, OrderDetailView, OrderListView, OrderAdminView

urlpatterns = [
    path('create/', view=OrderCreateView.as_view(), name='create_order'),
    path('<int:id>/', view=OrderDetailView.as_view(), name='order_detail'),
    path('list/', view=OrderAdminView.as_view(), name='order_list'),
    path('update/<int:id>/', view=OrderAdminView.as_view(), name='order_update'),
    path('customer/<int:id>/list/', view=OrderListView.as_view(), name='user_order_list'),
]