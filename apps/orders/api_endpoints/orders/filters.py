from django_filters import FilterSet, CharFilter
from apps.orders.models import Order

class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    address = CharFilter(lookup_expr='icontains')
    status = CharFilter()


    class Meta():
        model = Order
        fields = ['address', 'status']