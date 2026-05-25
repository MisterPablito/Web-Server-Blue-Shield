from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vulnerabilidade/<int:id>/', views.detalhe, name='detalhe'),
    path('stats/', views.stats, name='stats'),
]