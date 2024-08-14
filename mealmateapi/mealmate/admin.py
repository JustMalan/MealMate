from django.contrib import admin
from mealmate.models import Recipe, Ingredient, RecipeInstructions

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeInstructions)