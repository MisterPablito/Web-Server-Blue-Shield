from django.shortcuts import render, get_object_or_404
from django.db.models import Case, When, IntegerField
from .models import Vulnerabilidade

def home(request):
    vulnerabilidades = Vulnerabilidade.objects.annotate(
        risco_order=Case(
            When(risco='A', then=1),
            When(risco='M', then=2),
            When(risco='B', then=3),
            output_field=IntegerField()
        )
    ).order_by('risco_order', '-created_at')
    return render(request, 'social/home.html', {'vulnerabilidades': vulnerabilidades})

def detalhe(request, id):
    vuln = get_object_or_404(Vulnerabilidade, id=id)
    return render(request, 'social/detalhe.html', {'vuln': vuln})

def stats(request):
    total = Vulnerabilidade.objects.count()
    alto = Vulnerabilidade.objects.filter(risco='A').count()
    medio = Vulnerabilidade.objects.filter(risco='M').count()
    baixo = Vulnerabilidade.objects.filter(risco='B').count()
    return render(request, 'social/stats.html', {
        'total': total,
        'alto': alto,
        'medio': medio,
        'baixo': baixo
    })