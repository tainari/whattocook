from django.contrib import admin
from . import models
from .models import Recipe, Ingredient, Unit, IngredientCategory, RecipeIngredient, Texture, Flavour, CookMethod, Fillingness#, RecipeSteps
# Register your models here.

# class RecipeStepAdmin(admin.ModelAdmin):
#     list_display = ("recipe","stepnumber")
# class RecipeStepInLine(admin.TabularInline):
#     model = models.RecipeSteps
#     #autocomplete_fields = ["name"]
#     max_num = 5
#     extra = 1
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    # inlines = [RecipeStepInLine]
    prepopulated_fields = {
        'slug': ['name']
    }

class IngredientCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)


class CookMethodAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TextureAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FillingnessAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FlavourAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'num_units', 'unit')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(IngredientCategory, IngredientCategoryAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Flavour,FlavourAdmin)
admin.site.register(Fillingness,FillingnessAdmin)
admin.site.register(CookMethod,CookMethodAdmin)
admin.site.register(Texture,TextureAdmin)
