from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet ##Can also have ReadOnlyModelViewSet! no writing.
from rest_framework import status
from .models import Recipe
from .filters import RecipeFilter
from .serializers import RecipeSerializer

# Create your views here.
class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()#Recipe.objects.annotate(ingredient_count=Count('products')).all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = RecipeFilter
    search_fields = ['title','description']
    ordering_fields = ['unit_price','last_update']


# def index(request):
#     recipes = Recipe.objects.all()
#     #output = ", ".join([r.name for r in recipes])
#     return HttpResponse(recipes)
