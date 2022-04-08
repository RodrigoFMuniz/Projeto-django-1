from sre_constants import CATEGORY_WORD
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
# from utils.recipes.factory import make_recipe
from recipes.models import Recipe

# Create your views here.


def home(request):
    obj = {
        # 'recipes': [make_recipe() for _ in range(10)],
        'recipes': Recipe.objects.all().order_by('-id')
    }
    return HttpResponse(render_to_string('recipes\\pages\\home.html', context=obj))

def category(request, category_id):
    print('id', category_id)
    recipe= Recipe.objects.filter(category__id = category_id)
    print('Recipe', recipe)
    return render(request, 'recipes\\pages\\home.html', context={'recipe':recipe})

def recipe(request, recipe_id):
    recipe= Recipe.objects.filter(id = recipe_id).first()
    return render(request, 'recipes\\pages\\recipe.html', context={'recipe':recipe})

