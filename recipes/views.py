from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    output = ", ".join([r.title for r in recipes])
    return HttpResponse(output)
