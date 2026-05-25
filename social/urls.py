from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista_vulnerabilidades, name='lista'),
    path('vulnerabilidade/<int:id>/', views.detalhe, name='detalhe'),
    path('ranking/', views.ranking, name='ranking'),
    path('about/', views.about, name='about'),
    path('sugestoes/', views.sugestoes, name='sugestoes'),
    path('nao-encontrado/', views.nao_encontrado, name='nao_encontrado'),
    path('api/sugestao-nomes/', views.api_sugestao_nomes, name='api_sugestao_nomes'),
]