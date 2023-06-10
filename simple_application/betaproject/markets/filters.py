import django_filters
from .models import Market

class FilterMarketInfo(django_filters.FilterSet):
    class Meta:
        model = Market
        fields = ['timestamp', 'transactionhash', 'address']