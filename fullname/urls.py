from django.urls import path
from django.urls import path
from fullname.list.views import UserListView
from fullname.views import UserApiView, UserDetail, UserEdit

urlpatterns = [
    path('user/', UserApiView.as_view(), name='userApiView'),
    path('user/<int:pk>/', UserDetail.as_view(), name='userDetail'),
    path('user/edit/<int:pk>/', UserEdit.as_view(), name='userDetail'),
    path('user/all', UserListView.as_view(), name='userListView'),
]