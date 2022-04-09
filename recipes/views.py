from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
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
    # recipe = Recipe.objects.filter(
    #     category__id=category_id, is_published=True).order_by('-id')
    # if not recipe:
    #     # return render(request, 'recipes\\pages\\404.html', status=404)
    #     raise Http404('Error 404 - Categoria não encontrada')
    recipe = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id'))
    return render(request, 'recipes\\pages\\categories.html', context={'recipes': recipe, 'title': f'{recipe[0].category.name}'})


def recipe(request, pk):
    print('id', pk)
    recipe = Recipe.objects.filter(id=pk, is_published=True).first()
    print('recipe', recipe)
    # recipe = get_object_or_404(Recipe, id=pk, is_published=True)
    return render(request, 'recipes\\pages\\recipe.html', context={'recipe': recipe, 'is_detail_page': True})
