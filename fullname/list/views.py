from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from fullname.list.filters import UserFilter
from fullname.models import User
from fullname.serializer import UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    filterset_class = UserFilter
    ordering_fields = '__all__'
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return User.objects.all()
