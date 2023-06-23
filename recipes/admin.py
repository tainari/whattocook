from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredients
# Register your models here.

admin.site.register(Recipe)

admin.site.register(RecipeIngredients)

admin.site.register(Ingredient)
