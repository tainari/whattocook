from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredients, RecipeSteps
# Register your models here.

admin.site.register(Recipe)

admin.site.register(RecipeIngredients)

admin.site.register(RecipeSteps)

admin.site.register(Ingredient)
