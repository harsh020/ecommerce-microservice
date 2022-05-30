from django.urls import path

from product.product.v1.views import ProductDetailView, ProductCreateView, ProductListView, ProductImageView, \
    ProductListTopView

urlpatterns = [
    path('v1/create/', view=ProductCreateView.as_view(), name='product_create'),
    path('v1/delete/<int:id>/', view=ProductCreateView.as_view(), name='product_delete'),
    path('v1/image/upload/<int:id>/', view=ProductImageView.as_view(), name='product_image_upload'),
    path('v1/update/<int:id>/', view=ProductCreateView.as_view(), name='product_update'),
    path('v1/list/', view=ProductListView.as_view(), name='product_list'),
    path('v1/list/top/', view=ProductListTopView.as_view(), name='product_list_top'),
    path('v1/<int:id>/', view=ProductDetailView.as_view(), name='product_detail'),
]
