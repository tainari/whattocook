from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class IngredientCategory(models.Model):
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.category

class Unit(models.Model):
    unit = models.CharField(max_length=255)
    def __str__(self):
        return self.unit

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
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE)
    in_fridge = models.BooleanField(null=True, default=False)
    purchase_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    def __str__(self):
        return self.name  # models.CharField(max_length=255)
    #calories_per_gram = models.FloatField()


class Recipe(models.Model):
    TIME_SNAP = "S"
    TIME_FAST = "F"
    TIME_REGULAR = "R"
    TIME_LONG = "L"
    TIME_OVERNIGHT = "O"
    TIME_CHOICES = [
        (TIME_SNAP, "Snap"),
        (TIME_FAST, "Fast"),
        (TIME_REGULAR, "Regular"),
        (TIME_LONG, "Long"),
        (TIME_OVERNIGHT, "Overnightttt")
    ]
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    method = models.ForeignKey(CookMethod, on_delete=models.CASCADE)
    flavour_category = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    texture_category = models.ForeignKey(Texture, on_delete=models.CASCADE)
    fillingness_category = models.ForeignKey(
        Fillingness, on_delete=models.CASCADE)
    cook_time = models.CharField(max_length=1,
                                 choices=TIME_CHOICES)
    step_1 = models.CharField(max_length=500,default="")
    step_2 = models.CharField(max_length=500,null=True,blank=True)
    step_3 = models.CharField(max_length=500, null=True, blank=True)
    step_4 = models.CharField(max_length=500, null=True, blank=True)
    step_5 = models.CharField(max_length=500, null=True, blank=True)

# class RecipeSteps(models.Model):
#     recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
#     step_number = models.IntegerField(\
#         validators=[MinValueValidator(1), MaxValueValidator(5)],\
#         default=1)
#     step_text = models.CharField(max_length=1000, blank=True)
#     ordering = ['step_number']
#     def __str__(self):
#         return f'{self.recipe}: step {self.stepnumber}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    num_units = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # r = models.FloatField(default=0, null=True)
    def __str__(self):
        return f'{self.recipe}: {self.ingredient}'#self.recipe + ": " + self.ingredient


# Butter bread on both sides; place both slices in hot pan and fry until golden brown, then flip over
# Place cheese on either/both slices of bread
# When bread is toasted on other side, put slices together(cheese between both slices) and press down with spatula, then serve
