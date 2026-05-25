from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista_vulnerabilidades, name='lista'),
    path('vulnerabilidade/<int:id>/', views.detalhe, name='detalhe'),
    path('ranking/', views.ranking, name='ranking'),
    path('about/', views.about, name='about'),
]