from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Vulnerabilidade

def home(request):
    return render(request, 'social/home.html')

def lista_vulnerabilidades(request):
    qs = Vulnerabilidade.objects.all()
    q = request.GET.get('q')
    risco = request.GET.get('risco')
    if q:
        qs = qs.filter(Q(nome__icontains=q) | Q(descricao__icontains=q))
    if risco:
        qs = qs.filter(risco=risco)
    qs = qs.order_by('risco', 'nome')
    return render(request, 'social/lista.html', {'vulnerabilidades': qs})

def detalhe(request, id):
    vuln = get_object_or_404(Vulnerabilidade, id=id)
    vuln.views += 1
    vuln.save(update_fields=['views'])
    return render(request, 'social/detalhe.html', {'vuln': vuln})

def ranking(request):
    alto_qs = Vulnerabilidade.objects.filter(risco='A').order_by('-views', '-created_at')
    medio_qs = Vulnerabilidade.objects.filter(risco='M').order_by('-views', '-created_at')
    baixo_qs = Vulnerabilidade.objects.filter(risco='B').order_by('-views', '-created_at')
    alto_max = alto_qs.first().views if alto_qs else 0
    medio_max = medio_qs.first().views if medio_qs else 0
    baixo_max = baixo_qs.first().views if baixo_qs else 0
    ranking_data = [
        {'cor': 'red',   'titulo': '🔴 Risco Alto',   'rank_list': alto_qs,   'max_views': alto_max},
        {'cor': 'yellow','titulo': '🟠 Risco Médio',  'rank_list': medio_qs,  'max_views': medio_max},
        {'cor': 'green', 'titulo': '🟢 Risco Baixo',  'rank_list': baixo_qs,  'max_views': baixo_max},
    ]
    return render(request, 'social/ranking.html', {'ranking_data': ranking_data})

def about(request):
    return render(request, 'social/about.html')

def register_error(request):
    return render(request, 'registration/register_error.html')