from django.urls import include, path

from . import views

app_name = 'recipes'  # Utilizar recipes:recipe, ao invés de recipes-recipe

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/category/<int:category_id>/', views.category, name="category"),
    path('recipe/<int:pk>/', views.recipe, name="recipe"),
]
