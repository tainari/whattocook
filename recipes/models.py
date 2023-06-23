from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255,default=None)
    #calories_per_gram = models.FloatField()


class RecipeIngredients(models.Model):
    name = models.CharField(max_length=255)
    models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class RecipeSteps(models.Model):
    name = models.CharField(max_length=255)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    flavour_category = models.CharField(max_length=255)
    texture_category = models.CharField(max_length=255)
    fillingness_category = models.CharField(max_length=255)
    cook_time = models.IntegerField()
    ingredients = models.ForeignKey(RecipeIngredients, on_delete=models.CASCADE,default=None)
    steps = models.ForeignKey(RecipeSteps,on_delete=models.CASCADE,default=None)
