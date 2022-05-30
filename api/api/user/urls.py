from django.urls import path

from api.user.v1.views import UserDetailView, UserAuthView, UserListView, UserCreateView, UserAdminView

urlpatterns = [
    path('v1/register/', view=UserCreateView.as_view(), name='user_auth'),
    path('v1/login/', view=UserAuthView.as_view(), name='user_auth'),
    path('v1/profile/', view=UserDetailView.as_view(), name='user_detail'),
    path('v1/list/', view=UserListView.as_view(), name='user_list'),
    path('v1/<int:id>/', view=UserAdminView.as_view(), name='user_admin_detail'),
    path('v1/delete/<int:id>/', view=UserAdminView.as_view(), name='user_admin_delete'),
    path('v1/update/<int:id>/', view=UserAdminView.as_view(), name='user_admin_update'),
]

