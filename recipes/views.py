from sre_constants import CATEGORY_WORD
from telnetlib import STATUS

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

# from utils.recipes.factory import make_recipe
from recipes.models import Recipe

# Create your views here.


def home(request):
    obj = {
        # 'recipes': [make_recipe() for _ in range(10)],
        'recipes': Recipe.objects.filter(is_published=True).order_by('-id')
    }
    return HttpResponse(render_to_string('recipes\\pages\\home.html', context=obj))


def category(request, category_id):
    recipe = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')
    if not recipe:
        return render(request, 'recipes\\pages\\404.html', status=404)
    return render(request, 'recipes\\pages\\categories.html', context={'recipes': recipe, 'title': f'{recipe.first().category.name}'})


def recipe(request, pk):
    print('id', pk)
    recipe = Recipe.objects.filter(id=pk, is_published=True).first()
    print('recipe', recipe)
    return render(request, 'recipes\\pages\\recipe.html', context={'recipe': recipe, 'is_detail_page': True})
