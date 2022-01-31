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
    return HttpResponse(render_to_string('recipes\\home.html', context=obj))


def sobre(request):
    obj = {
        'nome': 'Rodrigo',
        'sobrenome': 'Muniz',
        'age': 35,
    }
    return render(request, 'recipes\\sobre.html', context=obj)


def contato(request):
    obj = {
        'nome': 'Rodrigo',
        'sobrenome': 'Muniz',
        'age': 35,
    }
    return render(request, 'base\\home.html', context=obj)
