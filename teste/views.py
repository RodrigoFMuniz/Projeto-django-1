from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


# Create your views here.
def teste(request):
    return HttpResponse(render_to_string('teste\\teste.html'))
