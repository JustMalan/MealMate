from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=40)
    recipe_type = models.CharField(max_length=40)
    recipe_calories = models.IntegerField()
    recipe_protein = models.IntegerField()
    recipe_fat = models.IntegerField()
    recipe_carbohydrates = models.IntegerField()
    recipe_image = models.ImageField()

    def __str__(self) -> str:
        return f"{self.recipe_name} - {self.recipe_calories}"
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    ingredient_name = models.CharField(max_length=40)
    ingredient_amount = models.CharField(max_length=40)
    ingredient_alternatives = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.ingredient_name}"
    
class RecipeInstructions(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="instructions")
    instructions = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.instructions}"
