from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from mealmate.models import Recipe, Ingredient, RecipeInstructions
from mealmate.api.serializers import RecipeSerializer, IngredientSerializer, RecipeInstructionsSerializer

class RecipeListCreateAPIView(APIView):
    
    def get(self,request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many = True)
        return Response(serializer.data)

class ProteinListCreateAPIView(APIView):
    
    def get(self, request):
        protein = request.query_params.get('protein')
        if protein is not None:
            try:
                protein = int(protein)
                print(protein)
                lower_bound = protein - 10
                upper_bound = protein + 10

                recipes = Recipe.objects.filter(recipe_protein__gte= lower_bound, recipe_protein__lte= upper_bound)
                serializer = RecipeSerializer(recipes, many= True)
                return Response(serializer.data)
            except ValueError:
                return Response({"Error": "Protein must be an integer value"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "Protein Parameter is required"}, status = status.HTTP_400_BAD_REQUEST)