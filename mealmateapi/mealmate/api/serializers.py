from rest_framework import serializers
from mealmate.models import Recipe, Ingredient, RecipeInstructions

class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingredient
        exclude = ('id',)

class RecipeInstructionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeInstructions
        exclude = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Recipe
        exclude = ("id",)

    ingredients = IngredientSerializer(many = True, read_only=True)
    instructions = RecipeInstructionsSerializer(many=True,read_only=True)
