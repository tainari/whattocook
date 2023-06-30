from django.contrib import admin
from .models import Recipe, Ingredient, Unit, Category, RecipeIngredient, Texture, Flavour, CookMethod, Fillingness
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CookMethodAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TextureAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FillingnessAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FlavoudAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'num_units', 'unit')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Flavour,FlavoudAdmin)
admin.site.register(Fillingness,FillingnessAdmin)
admin.site.register(CookMethod,CookMethodAdmin)
admin.site.register(Texture,TextureAdmin)
