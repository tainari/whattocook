from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id','name']#,'ingredients_count']
        #ingredients_count = serializers.IntegerField(read_only=True)