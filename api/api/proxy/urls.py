from django.urls import re_path

from api.proxy.v1.views import ProxyView

urlpatterns = [
    re_path(r'^(?P<url>.*)$', view=ProxyView.as_view(), name='proxy'),
]