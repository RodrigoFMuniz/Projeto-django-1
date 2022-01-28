from django.urls import include, path

from . import views

urlpatterns = [
    path('home/', views.home),
    path('sobre/', views.sobre),
    path('contato/', views.contato),
    path('', include('teste.urls'))
]
