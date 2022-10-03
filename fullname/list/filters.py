from django_filters import rest_framework

from fullname.models import User


class UserFilter(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
        }
