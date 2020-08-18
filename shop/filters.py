import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields={
            'product_name':['icontains'],
            # 'category':['icontains'],
            # 'desc':['icontains'],
        }
        # fields=('product_name','category','decs') 