from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Pantry(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class CookMethod(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Flavour(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Texture(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Fillingness(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name  # models.CharField(max_length=255)
    #calories_per_gram = models.FloatField()

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    method = models.ForeignKey(CookMethod, on_delete=models.CASCADE)
    flavour_category = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    texture_category = models.ForeignKey(Texture, on_delete=models.CASCADE)
    fillingness_category = models.ForeignKey(
        Fillingness, on_delete=models.CASCADE)
    cook_time = models.IntegerField()
    # ingredient1 = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # num_units1 = models.FloatField()
    # unit1 = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # ingredient2 = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # num_units2 = models.FloatField()
    # unit2 = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # ingredient3 = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # num_units3 = models.FloatField()
    # unit3 = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # ingredient4 = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # num_units4 = models.FloatField()
    # unit4 = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # ingredient5 = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # num_units5 = models.FloatField()
    # unit5 = models.ForeignKey(Unit, on_delete=models.CASCADE)
    step1 = models.CharField(max_length=1000, default=None, blank=True)
    step2 = models.CharField(max_length=1000, default=None, blank=True)
    step3 = models.CharField(max_length=1000, default=None, blank=True)
    step4 = models.CharField(max_length=1000, default=None, blank=True)
    step5 = models.CharField(max_length=1000, default=None, blank=True)
    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    num_units = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.recipe}: {self.ingredient}'#self.recipe + ": " + self.ingredient


# Butter bread on both sides; place both slices in hot pan and fry until golden brown, then flip over

# Place cheese on either/both slices of bread
# When bread is toasted on other side, put slices together(cheese between both slices) and press down with spatula, then serve
