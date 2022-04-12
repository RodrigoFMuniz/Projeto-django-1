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
        'recipes': Recipe.objects.filter(is_published=True).order_by('-id')
    }
    return HttpResponse(render_to_string('recipes\\pages\\home.html', context=obj))

def category(request, category_id):
    recipe= Recipe.objects.filter(category__id = category_id, is_published=True).order_by('-id')
    return render(request, 'recipes\\pages\\home.html', context={'recipes':recipe})

def recipe(request, pk):
    print('id', pk)
    recipe= Recipe.objects.filter(id = pk, is_published=True).first()
    print('recipe', recipe)
    return render(request, 'recipes\\pages\\recipe.html', context={'recipe':recipe, 'is_detail_page': True})
