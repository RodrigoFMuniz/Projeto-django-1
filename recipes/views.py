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
<<<<<<< HEAD
    return render(request, 'base\\home.html', context=obj)
=======
    return HttpResponse(render_to_string('base\\home.html', context=obj))
>>>>>>> 82a1f93c389953d259b1c76bfb84d821c3a556b7
