from django.urls import path
from mealmate.api.views import RecipeListCreateAPIView, ProteinListCreateAPIView

urlpatterns = [
    path("meals/",RecipeListCreateAPIView.as_view(),name="meals"),
    path("meals/protein-range/",ProteinListCreateAPIView.as_view(),name="recipes-protein-range")
]
