from unicodedata import name

from django.urls import include, path

from . import views

app_name = 'recipes'  # Utilizar recipes:recipe, ao invés de recipes-recipe

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:id>/', views.recipe, name="recipe"),
]
