import django_filters
from .models import Market
# allow django filters to read into database
class FilterMarketInfo(django_filters.FilterSet):
    class Meta:
        model = Market
        fields = ['timestamp', 'transactionhash', 'address']