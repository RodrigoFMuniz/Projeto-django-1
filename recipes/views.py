from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.


def home(request):
    obj = {
        'nome': 'Rodrigo',
        'sobrenome': 'Muniz',
        'age': 35,
    }
    return HttpResponse(render_to_string('recipes\\pages\\home.html', context=obj))


def recipe(request, id):
    obj = {
        'nome': 'Rodrigo',
        'sobrenome': 'Muniz',
        'age': 35,
    }
    return render(request, 'recipes\\pages\\recipe.html', context=obj)
