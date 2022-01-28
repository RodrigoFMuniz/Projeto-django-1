from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def teste(request):
    return HttpResponse('''
    <html>
    <head>
    <title>teste</title>
    </head>
    <body>
    <h1>teste</h1>
    </body>
    </html>
    ''')
