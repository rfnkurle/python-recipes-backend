from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('recipeId',
                  'recipeName',
                  'time',
                  'ingredients',
                  'instructions'
                 )