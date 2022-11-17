import django_filters
from .models import Clothes, Brend


class ClothesFilter(django_filters.FilterSet):

    class Meta:
        model = Clothes
        fields = {'gender':['exact'], 'brend':['exact'], 'category':['exact'], 'size':['exact'], 'color':['exact']}
        
