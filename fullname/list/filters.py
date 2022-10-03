from django.db.models.functions.text import Concat
from django_filters import rest_framework as filters
from fullname.models import User
from django.db.models import Value


def filter_by_name(queryset, name, value):
    queryset = queryset.annotate(
        name=Concat('first_name', Value(' '), 'last_name')
    )
    return queryset.filter(**{name: value})


class UserFilter(filters.FilterSet):
    name = filters.CharFilter(method=filter_by_name)

    class Meta:
        model = User
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
        }





