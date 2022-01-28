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
    return HttpResponse(render_to_string('home.html', context=obj))


def sobre(request):
    obj = {
        'nome': 'Rodrigo',
        'sobrenome': 'Muniz',
        'age': 35,
    }
    return render(request, 'sobre.html', context=obj)


def contato(request):
    return HttpResponse('''
    <html>
    <head>
    <title>Contato</title>
    </head>
    <body>
    <h1>Contato</h1>
    </body>
    </html>
    ''')
