from django_filters.rest_framework import FilterSet
from .models import Recipe

class RecipeFilter(FilterSet):
    class Meta:
        model = Recipe
        fields = {
            'name': ['exact'],
            #'unit_price': ['gt','lt'] #order matters - this is how they will show up in UI
        }