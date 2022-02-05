from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home),
    path('recipe/<int:id>/', views.recipe),
    path('teste/', include('teste.urls'))
]
