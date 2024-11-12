from django_filters import rest_framework as filters
from .models import Perfil

class PerfilFilter(filters.FilterSet):
    user_email = filters.CharFilter(field_name="user__email", lookup_expr="iexact")
    user_username = filters.CharFilter(method="filter_by_usernames")

    class Meta:
        model = Perfil
        fields = ['user_email', 'user_username']

    def filter_by_usernames(self, queryset, name, value):
        usernames = value.split(",")  # Divide a string em uma lista de usernames
        return queryset.filter(user__username__in=usernames)