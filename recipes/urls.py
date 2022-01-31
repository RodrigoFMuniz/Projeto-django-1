from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home),
    path('sobre/', views.sobre),
    path('contato/', views.contato),
    path('', include('teste.urls'))
]
