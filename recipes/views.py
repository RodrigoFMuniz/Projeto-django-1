from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

# Create your views here.


def home(request):
    obj = {
        # 'recipes': [make_recipe() for _ in range(10)],
        'recipes': Recipe.objects.all().order_by('-id')
    }
    return HttpResponse(render_to_string('recipes\\pages\\home.html', context=obj))


def recipe(request, id):
    obj = {
        'recipe': Recipe.objects.filter(id = id),
        'is_detail_page': True,
    }
    return render(request, 'recipes\\pages\\recipe.html', context=obj)
